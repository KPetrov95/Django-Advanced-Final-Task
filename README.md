# Django-Advanced-Final-Task

Task Logic:
This is a simple Bookstore implementation. 
It contains of Book List with a several filtering and ordering methods.
Basic Author and Genre lists being able to show in details additional information about them and the appropriate books. 

There is a Register/Login functionality and Profile attached to the User Model for the additional information.

Cart functionality is available which stores the necessary information in the session.
From the Cart interface you are able to see the total price of the eventual order, you can remove books or reduce their quantity if you added more than one of the same.
There is also a Favorite Books functionality implemented. Books can be put in the Cart directly from the Favorites List.
These features can be accessed through the details page of a book if the user is authenticated.

You can create/read/edit/delete reviews under the details page of the book. This is one of the DRF implementations.

Orders are confirmed through a checkout form and upon successful submission an E-mail is sent to the user. This is implemented through celery/redis.

 
The project is hosted on Azure on the following link:
    https://exam-bookstore-gwh4dwddhxaxancv.italynorth-01.azurewebsites.net/

Here are credentials for users in different groups:

Manager(staff):

        username: ManagerUser
        pass: 12manager34
Personnel:

        username:PersonnelUser
        pass: 12personnel34

SuperUser(superuser):

        username:admin
        password:12admin34


Please note that the registration emails are random and cannot be edited.
To test the email functionality please register a new user.


Running the Project locally:

clone repo:

        https://github.com/KPetrov95/Django-Advanced-Final-Task.git
    
install dependencies:

        pip install -r requirements.txt
    
starting:

        python manage.py runserver
        celery -A bookStore worker --loglevel=info -P eventlet

(eventlet is necessary for running celery on Windows)
If it's problematic for other OS try this:

        celery -A bookStore worker --loglevel=info


Link to environment variables( знам, че това, както и креденшълите горе са секюрити риск, но при попълване на анкетата не бях готов с тях):
    
     https://docs.google.com/document/d/1nhrJY56VaNMa7jsll8vmOmETULZVG2HOpFquec7KLjg/edit?usp=sharing