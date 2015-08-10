P3: Item Catalog
Description: An application that provides a list of items (books) within a variety of categories (genres) as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

Author: Susmita Gorai
Submission Date: 08/10/2015
Full Stack Web Developer Nanodegree 
March '15 Cohort

Location of code:
https://github.com/sus193

Code to download:
1. application.py - is the application controller
2. database_setup.py - contains the database schema
3. database_setup.pyc - compiled 
4. lotsofbooks.py - contains catalog data that is added to database
5. client_secrets.json - contains the security data
6. catalogwithusers.db - database 
7. /static/ - styles.css, top-banner.jpg, blank_user.gif
8. /templates/ (13 files) - login.html, header.html, main.html, publicBook.html, publicGenres.html, book.html, genres.html, newGenre.html, newBook.html, editGenre.html, editBook.html, deleteBook.html, deleteGenre.html

Steps to run:

Part 1: Set up the SQLlite database
-Install GIT, VirtualBox, Vagrant
-Use GIT to fetch the VM configuration and clone the repository provided by Udacity
-Download the source files from the above Github repository and add the new source files
-Change to the fullstack/vagrant/catalog directory and run the command "vagrant up" to launch the VM and "vagrant ssh" to log into it
-Change to the /vagrant/catalog directory

Part 2: Create the catalogwithusers database with Base, User, Genre, Book (OR use the provided one and skip part 3)
-Can be done through the python file through the command:
vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python database_setup.py
-Look in the file directory for the following generated file: catalogwithusers.db

Part 3: Populate the database with data (if created new one)
-Run the following command:
vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python lotsofbooks.py
-Wait to receive confirmation the data has been added when you see "added books!"

Part 4: Run the application 
-Run the following command to start up the application server
vagrant@vagrant-ubuntu-trusty-32:/vagrant/catalog$ python application.py
-Expected result: 
* Running on http://0.0.0.0:8000/
* Restarting with reloader
-Now go to localhost:8000 in any browser to test the application
-Expected Result is to see the genres screen appear first

Part 5: API Endpoints
-Go to localhost:8000/genres/JSON to see all of the genres
-Go to localhost:8000/genre/genre_id/books/JSON to see all of the books for a particular genre
example: http://localhost:8000/genre/1/books/JSON should show 8 books for genre_id: 1
-Go to localhost:8000/genre/genre_id/books/book_id/JSON to see the JSON representation for a particular book
example: http://localhost:8000/genre/1/books/1/JSON will return the book "Humans of New York"

Part 6: CRUD: Read
-Page reads category information from the database - localhost:8000/genres shows all of the genre categories that are stored in the database and also the most recent 10 books that have added
-Page reads item information from the database - example localhost:8000/genre/1/books/ shows all of the book items that are stored in the database for the Art, Architecture & Photography genre
-These pages are the public pages that show the genres and books currently stored (since they have no edit|delete options for the genres nor books)
-After login, the private genres and books pages are also reading data from the database
-Go to any genre's page and see the creator username and picture, which are read from the database

Part 7: Authentication & Authorization
-Login to access the remaining CRUD operations-Click on "Login" and then "Sign in" and enter your Google Plus credentials and allow access to your account
-Successful login will show a flash message "You are now logged in as [First Name Last Name]"
-This will create a new user record for the User table and allow creating your own genres and books
-Also, login with the following test account to gain access to this user's genres and books to be able to edit, delete them
username: sus46072
password: udacityRocks15
***NOTE: This account has been made just for this Udacity project as a test account so please feel free to login with it to test out my application. If you use it, your user name will be "Sus Second"***
-To logout, press "Logout" and a message will flash "You have successfully logged out"

Part 7: CRUD: Create
-After successful login, create a new genre by clicking on "Add Genre" from the main page
-The url will change to localhost:8000/genre/new/ and provide a form to create a new genre. Once you press "Create" you will see a flash message that the new genre has been created for this user
-Once redirected back to the main page, go to the newly created genre page which initially doesn't have any books 
-Create a new book for this genre by clicking on "Add Book" and the url will change to localhost:8000/genre/genre_id/new
-Enter the fields for creating the new book - Name, Description, Author, ISBN and click "Create" and now this genre page will show this newly added book

Part 8: CRUD: Update (Edit)
-Update operation will depend on whether the user is authorized or not to update the genre or book->If the user who is currently logged in is the creator of the genre then he/she can update the genre (or book for this genre)
-If you are logged in with "sus46072" you will notice you have authorization to update or edit the genres 1 through 8 - Click "edit" either on the main genres page or go to that genre's page and click "edit" to update the genre's name
-Similarly if you are logged in with "sus46072" you will have authorization to edit the information of the book items for genres 1 through 8 - Go to the genre page and click on "edit" on any of the listed books
-Once on the edit page (e.g. http://localhost:8000/genre/8/edit/ or http://localhost:8000/genre/8/43/edit/) enter the desired changes and press "Save"
-See the flash message "Genre (or Book) has been saved"

Part 9: CRUD: Delete
-Delete operation also depends on whether the user is authorized or not to delete the genre or book->If the user who is currently logged in is the creator of the genre then he/she can delete the genre (or book for this genre)
-Once logged in with "sus46072" click on "delete" from the main genres page or go to that genre's page first and click "delete"
-For example, go to http://localhost:8000/genre/8/delete/ or http://localhost:8000/genre/8/delete/ you will see a confirmation message "Are you sure you want to delete (Genre or Book)?" and press "Delete" and you will get a flash message to confirm the genre or book has been deleted
-It is requested that you first delete the book for a genre before deleting the genre itself (to ensure the Recent 10 list is updated properly)

Sources:
1. Udacity's Full Stack Foundations and Authentication & Authorization: OAuth for instructions
2. The fullstack-nanodegree-vm oauth and ud330 repository for providing code samples
3. Udacity's Discussion Forum
4. Python - http://www.tutorialspoint.com/python and https://docs.python.org
5. Google for images
6. Barnesandnoble.com for the genres and books information
7. Sql Alchemy - http://docs.sqlalchemy.org/en/rel_1_0/orm/query.html
8. Google Developers - https://console.developers.google.com