from flask import Flask, render_template, request, redirect, url_for,flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Book, User
#for authentication/authorization
from flask import session as login_session
import random, string
#imports for client secret
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Application"

#Connect to the database that is generated in database_setup.py
engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create a state token to prevent request forgery
#Store it in session for later validation
@app.route('/login')
def showLogin():
    state=''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE = state)

#Methot to do google plus authentication
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output

#Method to disconnect from google plus account
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200': #successfully disconnected
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        #return response
        flash ("You have successfully logged out")
        return redirect(url_for('showGenres'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        #return response
        flash ("You were not logged in")
        return redirect(url_for('showGenres'))

# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

#JSON Endpoint to get all the books
@app.route('/genre/<int:genre_id>/books/JSON')
def genreMenuJSON(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    books = session.query(Book).filter_by(
        genre_id=genre_id).all()
    return jsonify(Books=[i.serialize for i in books])

#JSON Endpoint to get a specific book
@app.route('/genre/<int:genre_id>/books/<int:book_id>/JSON')
def bookJSON(genre_id, book_id):
    book = session.query(Book).filter_by(id=book_id).one()
    return jsonify(Book=book.serialize)

#JSON Endpoint to get all the genres
@app.route('/genres/JSON')
def genresJSON():
    genres = session.query(Genre).all()
    return jsonify(genres=[r.serialize for r in genres])

#Method to show all the genres
#If logged in show genres.html otherwise if not logged in show publicGenres.html
@app.route('/')
@app.route('/genres/')
def showGenres():
    genres = session.query(Genre).all()
    recent_items = session.query(Book).order_by(Book.id.desc()).limit(10).all()
    if 'username' not in login_session:
        return render_template('publicGenres.html', genres=genres, recent_items=recent_items)
    else:
        return render_template('genres.html', genres=genres, recent_items=recent_items)

#Method to create a new genre
#If user is not logged in, redirected to login and after login user is allowed to create a new genre
@app.route('/genre/new/', methods=['GET', 'POST'])
def newGenre():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newGenre= Genre(name=request.form['name'], user_id = login_session['user_id'])
        session.add(newGenre)
        session.commit()
        flash('New Genre %s added' %newGenre.name);
        return redirect(url_for('showGenres'))
    else:
        return render_template('newGenre.html')
        #return "This page will be for making a new genre"

#Method to edit an existing genre
#If user is not logged in, redirected to login and after login will only be able to edit the genre if current user logged in is the creator of the genre
@app.route('/genre/<int:genre_id>/edit/', methods=['GET', 'POST'])
def editGenre(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedGenre = session.query(
        Genre).filter_by(id=genre_id).one()
    if editedGenre.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this genre. Please create your own genre in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedGenre.name = request.form['name']
            flash('Genre %s has been edited' % editedGenre.name)
            return redirect(url_for('showGenres'))
    else:
        return render_template(
            'editGenre.html', genre=editedGenre)

#Method to delete a genre
#If user is not logged in, redirected to login and after login will only be able to delete the genre if current user logged in is the creator of the genre
@app.route('/genre/<int:genre_id>/delete/', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    genreToDelete = session.query(Genre).filter_by(id=genre_id).one()
    if genreToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this genre. Please create your own genre in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(genreToDelete)        
        flash('Genre %s deleted' % genreToDelete.name);
        session.commit()
        return redirect(
            url_for('showGenres', genre_id=genre_id))
    else:
        return render_template(
            'deleteGenre.html', genre=genreToDelete)

#Method to show all the books for a particular genre
#If user is logged in show book.html, otherwise show publicBook.html to prevent making changes
#If user logged in is the creator of the genre then authorized to see book.html
@app.route('/genre/<int:genre_id>')
@app.route('/genre/<int:genre_id>/books/')
def showBooks(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    creator = getUserInfo(genre.user_id)
    books = session.query(Book).filter_by(genre_id=genre.id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicBook.html', books=books, genre=genre, creator=creator)
    else:
        return render_template('book.html', books=books, genre=genre, creator=creator)

#Method to create a new Book
#If user is not logged in, redirected to login and after login user is allowed to create a new book only if user is also the creator of this genre
@app.route('/genre/<int:genre_id>/new/', methods=['GET', 'POST'])
def newBook(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if login_session['user_id'] != genre.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add  books to this genre. Please create your own genre in order to add books.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        newItem = Book(name=request.form['name'], description = request.form['description'], author=request.form['author'], isbn=request.form['isbn'], genre_id=genre_id, user_id = genre.user_id)
        session.add(newItem)
        session.commit()
        flash('New Book %s added' % newItem.name);
        return redirect(url_for('showBooks', genre_id=genre_id))
    else:
        return render_template('newBook.html', genre_id=genre_id)

#Method to edit an existing Book
#If user is not logged in, redirected to login and after login user is allowed to edit an existing book only if user is also the creator of this genre
@app.route('/genre/<int:genre_id>/<int:book_id>/edit/', methods=['GET', 'POST'])
def editBook(genre_id, book_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(Book).filter_by(id=book_id).one()
    genre = session.query(Genre).filter_by(id=genre_id).one()
    if login_session['user_id'] != genre.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit books for this genre. Please create your own genre in order to edit books.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name=request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['author']:
            editedItem.author = request.form['author']
        if request.form['isbn']:
            editedItem.isbn = request.form['isbn']
        session.add(editedItem)
        flash('Book %s has been edited' % editedItem.name)
        session.commit()
        return redirect(url_for('showBooks', genre_id=genre_id))
    else:
        return render_template('editBook.html', genre_id=genre_id, book_id = book_id, i=editedItem)

#Method to delete a Book
#If user is not logged in, redirected to login and after login user is allowed to delete this book only if user is also the creator of this genre
@app.route('/genre/<int:genre_id>/<int:book_id>/delete/', methods=['GET', 'POST'])
def deleteBook(genre_id, book_id):
    if 'username' not in login_session:
        return redirect('/login')
    genre = session.query(Genre).filter_by(id=genre_id).one()
    itemToDelete = session.query(Book).filter_by(id=book_id).one()
    if login_session['user_id'] != genre.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete books for this genre. Please create your own genre in order to delete books.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)        
        flash('Book %s has been deleted' % itemToDelete.name)
        session.commit()
        return redirect(url_for('showBooks', genre_id=genre_id))
    else:
        return render_template('deleteBook.html', item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)