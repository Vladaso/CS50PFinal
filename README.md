# Catculator
    #### Video Demo:  https://youtu.be/WyQgXoJp5EI
    #### Description:
    To describe the project simply, from filling out a simple form it asserts what kind of cat suits you best
    and then remembers it connected to your account, you can fill the simple form as many times as you want,
    each time getting a different cat. Now I will describe some functionality/libraries/files in the project:

    To run the project you need to install some libraries, mainly relating to the Flask web framework.
    Make sure you have python installed if you are running this locally!
    Run:
    pip install -r requirements.txt
    in the root directory terminal.
    After that you can run:
    pytest test_project.py
    to see if everything is running properly.
    At last you can run:
    python project.py
    That will start a development server, which you will find under the link pasted into console,
    most certainly it will be "http://127.0.0.1:5000".
    There you can see the whole website and test its funcionality, and most importantly find out WHAT CAT YOU ARE!

    project.py
        The main file of this project, will initialize your Flask application, important to note is that the secret key, required for Flask login and other functionality is just "test", if it will ever go into production this
        has to be changed!
        We also initialize the builtin login manager from the flask-login library, this will handle a lot of functionality for us, such as keeping json tokens or cookies so users stay signed in and they don't have to login each time they refresh the site.

        class User:
            UserMixin is passed down from docs, basically our database model - it tells us all the information we will be storing for a registered user in this case, their username, email, password - which every user has, the username has to be unique (not the email so when testing this project you don't have to make up non-existent emails to create more account). And each user also has their cat and the description relating to it - this is initialised to None when registering.
        load_user:
            A required function for Flask-login, tells the login manager when a user successfully logs in what kind of information it should remember.
        index():
            Our main "template", or rather route at root or "/". This is where the survey is contained we can access it by two methods, "GET" and "POST" get simply renders index.html in the static file (the naming convention will be explained later) and post will evaluate the form and return you your cat(if you filled out all the fields of course) then redirects you to the result route and shows you what cat you got and its general description.
        get_cat():
            This function is lengthy as I first wanted to write a mathematical function that out of 30 points gives you one of 19 cats, but this turned out hard so this was the simpler alternative, the function receives an evaluation and then returns a cat name and its description as a list.
        evaluate():
            Receives the form as a dictionary and evaluates it so sums all the users answers the questions are valued 0-3.
        login():
            Checks the inputted credentials against the database(a simple json) important to note is that I hash the passwords - why I am using the builtin function check password. Displays login.html
        register():
            Creates a new user if their username is unique, both login and register display flash messages if the inputted info isn't correct.
        logout():
            Uses logout_user() builtin method of the login_manager to log out a User and delete all of its cookies.
        my_cat():
            Renders the current cat on the user profile - if it's none simply displays that they need to take the survey.
        create_users_file():
            creates the database which is a json if it is not in the root directory of the project.

    static and templates folder:
        The naming convention is from flask static has to contain all the images and CSS files and templates has all the HTML files.
    templates:
        Will not explain all the functionality of each and every html file but it is important to note that I use Jinja to run python(which is converted to javascript I think) inside the HTML files so I can change what I display plus I can create standardized components which I just link/include in the bigger files so if I change something I don't have to write it out everywhere.
    Question.py and Quizzer.py:
        Created classes from questions so it is easier to add questions, although I have to say that after that my approach was counterintuitive as I require there to only be 10 questions.
    test_project.py:
        The main testing file, with pytest can test my project.py
    users.json:
        Just a simplified database, wanted to implent through PostgreSQL or even MongoDB but this would make the project much harder to run as I wouldn't give out my keys(even the free ones) out in a public repository. So this file simulates the functionality of a database.
            
        