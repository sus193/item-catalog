from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Book, User

engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
# Account credentials inside of README file to login and test authorization with this username
User1 = User(name="Sus Second", email="sus46072@gmail.com",
             picture='http://www.cdc.gov/importation/images/dog2.jpg')
session.add(User1)
session.commit()

# Books for Art, Architecture & Photography
genre1 = Genre(user_id=1, name="Art, Architecture & Photography")

session.add(genre1)
session.commit()

book1 = Book(user_id=1, name="Humans of New York", description=" A beautiful, heartfelt, funny, and inspiring collection of photographs and stories capturing the spirit of a city",
                     author="Brandon Stanton", isbn="9781250038821", genre=genre1)

session.add(book1)
session.commit()


book2 = Book(user_id=1, name="It\'s What I Do: A Photographer\'s Life of Love and War", description="War photographer Lynsey Addario\'s memoir It\'s What I Do is the story of how the relentless pursuit of truth, in virtually every major theater of war in the twenty-first century, has shaped her life",
                     author="Lynsey Addario", isbn="9781101599068", genre=genre1)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="The Grammar of Architecture", description="he Grammar of Architecture uses beautifully engraved plates from the great works of architectural history to illustrate a journey of the architecture of civilizations around the world",
                     author="Emily Cole", isbn="9780760774458", genre=genre1)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="Leonardo da Vinci", description="The moving story of the man behind the Renaissance myth",
                     author="Jay Williams", isbn="2940149748082", genre=genre1)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="Marvel Encyclopedia", description="Bring the Marvel Universe home with this all-inclusive encyclopedia detailing little-known facts and information about the iconic Marvel characters. ",
                     author="DK Publishing", isbn="9781465415936", genre=genre1)

session.add(book5)
session.commit()

book6 = Book(user_id=1, name="The Great Bridge: The Epic Story of the Building of the Brooklyn Bridge", description="This book brings back for American readers the heroic vision of the America we once had. ",
                     author="David McCullough", isbn="9780671457112", genre=genre1)

session.add(book6)
session.commit()

book7 = Book(user_id=1, name="Exploring Calvin and Hobbes: An Exhibition Catalogue",
                     description="Enjoy this beautiful companion book to the extensive Exploring Calvin and Hobbes exhibition at the Billy Ireland Cartoon Library.", 
                     author="Bill Watterson, Robb Jenny", isbn="9781449460365", genre=genre1)

session.add(book7)
session.commit()

book8 = Book(user_id=1, name="A History of the World in 100 Objects", description="A History of the World in 100 Objects stretches back two million years and covers the globe. ",
                     author="Neil MacGregor", isbn="9780143124153", genre=genre1)

session.add(book8)
session.commit()


# Books for Biography
genre2 = Genre(user_id=1, name="Biography")

session.add(genre2)
session.commit()


book1 = Book(user_id=1, name="The Wright Brothers", description="the dramatic story-behind-the-story about the courageous brothers who taught the world how to fly: Wilbur and Orville Wright.",
                     author="David McCullough", isbn="9781476728742", genre=genre2)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="Life Is Short (No Pun Intended): Love, Laughter, and Learning to Enjoy Every Moment",
                     description=" an uplifting and moving behind-the-scenes account of how the pair met, fell in love, and overcame huge obstacles to become successful professionals and parents.", 
                     author="Jennifer Arnold, Bill Klein", isbn="9781476794709", genre=genre2)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="I Am Malala: The Girl Who Stood Up for Education and Was Shot by the Taliban", 
                     description="When the Taliban took control of the Swat Valley in Pakistan, one girl spoke out. Malala Yousafzai refused to be silenced and fought for her right to an education",
                     author="Malala Yousafzai", isbn="9780316322423", genre=genre2)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="Wild: From Lost to Found on the Pacific Crest Trail ", description="Wild powerfully captures the terrors and pleasures of one young woman forging ahead against all odds on a journey that maddened, strengthened, and ultimately healed her. ",
                     author="Cheryl Strayed", isbn="9780307476074", genre=genre2)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="Night", description="Night is Elie Wiesel\'s masterpiece, a candid, horrific, and deeply poignant autobiographical account of his survival as a teenager in the Nazi death camps.",
                     author="Elie Wiesel", isbn="9780374500016", genre=genre2)

session.add(book5)
session.commit()

book6 = Book(user_id=1, name="My Fight / Your Fight", description="In this inspiring and moving book, Ronda Rousey, the Olympic medalist in judo, reigning UFC women's bantamweight champion, and Hollywood star charts her difficult path to glory.",
                     author="Ronda Rousey", isbn="9781941393260", genre=genre2)

session.add(book6)
session.commit()


# Books for Business
genre3 = Genre(user_id=1, name="Business")

session.add(genre3)
session.commit()


book1 = Book(user_id=1, name="It's Never Too Late: Creating the Life of Your Dreams", description="What does it take to go from a convicted drug addict without a penny in your pocket to a successful millionaire businessman, whose passion is helping other people turn their lives around.",
                     author="Chris Atkinson, Debbie Atkinson", isbn="2940151329583", genre=genre3)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="The Art of War", description="The art of war is of vital importance to the State, writes General Sun Tzu at the outset of one of the most important military treatises ever written.",
                     author="Sun Tzu", isbn="9781435136502", genre=genre3)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Outliers: The Story of Success", description="There is a story that is usually told about extremely successful people, a story that focuses on intelligence and ambition. ",
                     author="Malcolm Gladwell", isbn="9780316017930", genre=genre3)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change", description="The miniature edition of the bestselling guide to personal fulfillment and professional success!.",
                     author="Stephen R. Covey", isbn="9781451639612", genre=genre3)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="Lean In: Women, Work, and the Will to Lead", description="In Lean In, Sheryl Sandberg examines why women\'s progress in achieving leadership roles has stalled, explains the root causes, and offers compelling, commonsense solutions that can empower women to achieve their full potential. ",
                     author="Sheryl Sandberg", isbn="9780385349949", genre=genre3)

session.add(book5)
session.commit()


# Books for Fiction
genre4 = Genre(user_id=1, name="Fiction")

session.add(genre4)
session.commit()


book1 = Book(user_id=1, name="All the Light We Cannot See", description="the beautiful, stunningly ambitious instant New York Times bestseller about a blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II..",
                     author="Anthony Doerr", isbn="9781476746586", genre=genre4)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="The Girl on the Train", description="Compulsively readable, The Girl on the Train is an emotionally immersive, Hitchcockian thriller and an electrifying debut.",author="Paula Hawkins", isbn="9780698185395", genre=genre4)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Memory Man",
                     description="This strong first in a new thriller series from bestseller Baldacci (The Escape) introduces Amos Decker, the memory man, whose unique abilities are the result of a vicious hit he suffered as a 22-year-old NFL rookie that ended his football career. ", author="David Baldacci", isbn="9781455586387", genre=genre4)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="Unleashed", description="The threat of a major terrorist attack on the U.S. doesn\'t dispel the charm of Edgar-finalist Rosenfelt\'s 11th mystery featuring Paterson, N.J., criminal defense attorney Andy Carpenter (after 2012\'s Leader of the Pack).",
                     author="David Rosenfelt", isbn="9781250024732", genre=genre4)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="The Good Girl", description="An addictively suspenseful and tautly written thriller, The Good Girl is a propulsive debut that reveals how even in the perfect family, nothing is as it seems.",
                     author="Mary Kubica", isbn="9781460330197", genre=genre4)

session.add(book5)
session.commit()

book6 = Book(user_id=1, name="Go Set a Watchman", description="Returning home to Maycomb to visit her father, Jean Louise Finch Scout struggles with issues both personal and political, involving Atticus, society, and the small Alabama town that shaped her.",
                     author="Harper Lee", isbn="9780062409850", genre=genre4)

session.add(book6)
session.commit()


# Books for Diet, Health, Fitness
genre5 = Genre(user_id=1, name="Diet, Health, Fitness")

session.add(genre5)
session.commit()


book1 = Book(user_id=1, name="10-Day Green Smoothie Cleanse: Lose Up to 15 Pounds in 10 Days!", description="The New York Times bestselling 10-Day Green Smoothie Cleanse will jump-start your weight loss, increase your energy level, clear your mind, and improve your overall health.",
                     author="JJ Smith", isbn="9781501100109", genre=genre5)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="Switch On Your Brain: The Key to Peak Happiness, Thinking, and Health", description="Scientist and therapist helps readers understand how the power of their thoughts can help them manage stress, break unhealthy patterns, use their brains more effectively, and overcome mental, emotional, physical, and spiritual obstacles",
                     author="Caroline Leaf", isbn="9780801018398", genre=genre5)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Being Mortal: Medicine and What Matters in the End", description="In Being Mortal, bestselling author Atul Gawande tackles the hardest challenge of his profession: how medicine can not only improve life but also the process of its ending",
                     author="Atul Gawande", isbn="9780805095159", genre=genre5)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="The Whole30: The 30-Day Guide to Total Health and Food Freedom",
                     description="The Whole30 provides the step-by-step, recipe-by-recipe guidebook that will allow millions of people to experience the transformation of their entire life in just one month.", author="Melissa Hartwig, Dallas Hartwig", isbn="9780544609716", genre=genre5)

session.add(book4)
session.commit()

book5 = Book(user_id=1, name="Supermarket Healthy: Recipes and Know-How for Eating Well Without Spending a Lot", description="Melissa demystifies the task of preparing nutritious and delicious food by showing exactly how you can make your grocery store work for you.", author="Melissa d'Arabian, Raquel Pelzel", isbn="9780307985170", genre=genre5)

session.add(book5)
session.commit()


# Books for Mystery & Crime
genre1 = Genre(user_id=1, name="Mystery and Crime")

session.add(genre1)
session.commit()


book1 = Book(user_id=1, name="The Nature of the Beast", description="But when the boy disappears, the villagers are faced with the possibility that one of his tall tales might have been true.", author="Louise Penny", isbn="9781250085832", genre=genre1)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="Nemesis", description="At New York City\'s J.F.K. Airport, a man waiting in the security line suddenly grabs a woman and brandishes a grenade. ",
                     author="Catherine Coulter", isbn="9780698164895", genre=genre1)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Speaking in Bones", description="In the latest blockbuster novel from #1 New York Times bestselling author Kathy Reichs, forensic anthropologist Temperance Brennan investigates what looks to be a typical missing person case, only to find herself digging up bones possibly left by a serial killer, a cult, or perhaps something not entirely of this world.", author="Kathy Reichs", isbn="9780345544056", genre=genre1)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="The Highway", description="When two sisters set out across a remote stretch of Montana road to visit their friend, little do they know it will be the last time anyone might ever hear from them again.", author="C. J. Box", isbn="9781250031921", genre=genre1)

session.add(book4)
session.commit()

book2 = Book(user_id=1, name="A Banquet of Consequences", description="The #1 New York Times bestselling author\'s award-winning series returns with another stunning crime drama featuring Scotland Yard members Detective Inspector Thomas Lynley and Detective Sergeant Barbara Havers.",
                     author="Elizabeth George", isbn="Entree", genre=genre1)

session.add(book2)
session.commit()


# Books for Romance
genre1 = Genre(user_id=1, name="Romance")

session.add(genre1)
session.commit()

book9 = Book(user_id=1, name="Heartless",
                     description="Life has taught Lucas Kendrick, Duke of Harndon, that a heart is a decided liability.", author="Mary Balogh", isbn="9780698156302", genre=genre1)

session.add(book9)
session.commit()


book1 = Book(user_id=1, name="The Last Summer", description="Judith Kinghorn presents a beautiful and haunting story of lost innocence and powerful, enduring love, in her sweepingly epic and gloriously intimate debut.",
                     author="Judith Kinghorn", isbn="9780594585558", genre=genre1)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="The Liar", description="Even in this small town, surrounded by loved ones, danger is closer than she knows and threatens Griff, as well. And an attempted murder is only the beginning.", author="Nora Roberts", isbn="9780698161351", genre=genre1)

session.add(book2)
session.commit()

book3 = Book(user_id=1, name="Earth Bound",
                     description=" But she never forgot the terror she left behind or the always present fear that the cult would find her again, and claim her.", author="Christine Feehan", isbn="9780698180529", genre=genre1)

session.add(book3)
session.commit()

book4 = Book(user_id=1, name="A New Hope", description="Starting over is never easy, but in Thunder Point, where newcomers are welcome and friends become family, it's possible to find yourself again.", author="Robyn Carr", isbn="9781460382073", genre=genre1)

session.add(book4)
session.commit()

book2 = Book(user_id=1, name="That Chesapeake Summer", description="From New York Times bestselling author Mariah Stewart comes the latest book in her celebrated Chesapeake Diaries, a small-town romance series in the tradition of Barbara Freethy, Susan Mallery, and Robyn Carr.",
                     author="Mariah Stewart", isbn="9781476792583", genre=genre1)

session.add(book2)
session.commit()

book10 = Book(user_id=1, name="In Plain Sight", description="For years Myra Rutledge and Annie de Silva, founding members of the Sisterhood, have funded an underground network run by former Supreme Court Justice Pearl Barnes to help women escape abusive relationships.",
                      author="Fern Michaels", isbn="9781420135954", genre=genre1)

session.add(book10)
session.commit()


# Books for Science Fiction & Fantasy
genre1 = Genre(user_id=1, name="Science Fiction & Fantasy")

session.add(genre1)
session.commit()


book1 = Book(user_id=1, name="1984",
                     description="1984 presents a startling and haunting vision of the world, so powerful that it is completely convincing from start to finish. ", 
                     author="George Orwell", isbn="9780451524935", genre=genre1)

session.add(book1)
session.commit()

book2 = Book(user_id=1, name="Witches of East End", description="The three Beauchamp women-Joanna and her daughters, Freya and Ingrid-live ordinary lives in mist-shrouded North Hampton, out on the tip of Long Island.",
                     author="Melissa de la Cruz", isbn="9780594562153", genre=genre1)

session.add(book2)
session.commit()


book3 = Book(user_id=1, name="Station Eleven", description="Kirsten Raymonde will never forget the night Arthur Leander, the famous Hollywood actor, had a heart attack on stage during a production of King Lear. That was the night when a devastating flu pandemic arrived in the city, and within weeks, civilization as we know it came to an end. ",
                     author="Emily St. John Mandel", isbn="9780804172448", genre=genre1)

session.add(book3)
session.commit

book4 = Book(user_id=1, name="The Martian",
                     description="After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead, Mark finds himself stranded and completely alone with no way to even signal Earth that he\'s alive", author="Andy Weir", isbn="9780553418026", genre=genre1)

session.add(book4)
session.commit()


book5 = Book(user_id=1, name="Welcome to Night Vale",
                     description="From the creators of the wildly popular Welcome to Night Vale podcast comes an imaginative mystery of appearances and disappearances that is also a poignant look at the ways in which we all struggle to find ourselves...no matter where we live.", author="Joseph Fink, Jeffrey Cranor", isbn="9780062442840", genre=genre1)

session.add(book5)
session.commit()


print "added books!"
