# Greatkart
Welcome to Greatkart where you can find inspired clothes products available to buy. This ecommerce store was built using Django and Python, deployed on Heroku.

This website provides full CRUD functionality to the admin user to add and delete products from the purposely built admin panel. Customers are able to view a history of all orders placed from their profile login. The goal of this assignment is to create a web interface that allows users to simply store and access and performance the CRUD (Create, Read, Update, and Delete) actions. This project's goal is to allow users to create, store, modify, and remove posts (CRUD). People that are interested in topics such as travel or planning to live abroad are the target audience for this initiative. Users can create new orders.

This website is for educational purposes only.

View the live site [here](https://greatkart-online.herokuapp.com/)

<br>

# Overview

- [User experience](#user-experience)
  * [User Stories](#user-stories)
- [Features](#features)
  * [Current Features](#current-features)
  * [Signed In Users](#signed-in-users)
  * [Future Prospects](#future-prospects)
- [Database](#database)
- [Testing]
- [Technologies Used](#technologies-used)
  * [Languages](#languages-used)
  * [Libraries & Integrations](#frameworks-libraries-and-programs)
- [Deployment](#deployment)
  * [Set up project locally](#set-up-project-locally)
  * [Deploy to Heroku](#deploy-to-heroku)
  * [AWS Static files storage](#aws-static-files-storage)
  * [Connect Stripe to Heroku](#connect-stripe-to-heroku)
- [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

# User experience

## User Stories

#### As a Customer:

- Website experience:

    1. I want to see how online shopping are made on the website.
    2. I want to be able to navigate the website.
    3. I want to be able to contact the seller.
    
    <br>

- Account:

    1. I want to save my details to a user profile.
    2. I want to be able to see my previous orders details.

    <br>

#### As the owner of the Website:

  1. I want to be able to add products with ease.
  2. I want to be able to edit and delete the orders.
  3. I want to have access to an admin page. 
  4. I want to be able to delete inappropriate orders as well.
  
# Features

- ### All apps 

    - Dashboard and Logout links (for signed in users) 
    - Login and sign up links (for unsigned users)
        ![Getting home page](https://github.com/surba778/greatkart/blob/main/readme-images/greatkart%20homepage.png)
        ![Admin account page](https://github.com/surba778/greatkart/blob/main/readme-images/admin%20account.png)
        ![Admin payment page](https://github.com/surba778/greatkart/blob/main/readme-images/admin%20payment%20form.png)
        ![Admin products page](https://github.com/surba778/greatkart/blob/main/readme-images/admin%20products.png)
        ![Sign in page](https://github.com/surba778/greatkart/blob/main/readme-images/signed%20in%20page.png)
       
## Signed In Users

- This is a summary of the features available only to login users:

    - Signed In users:
        - Sign out
        - Add and remove (only you own) the orders
        - Access orders history 
        - Add, edit and delete orders
        - Access Django admin page: (which involves access to every database and allows to answer costumer messages)
        ![Homepage with signed in](https://github.com/surba778/greatkart/blob/main/readme-images/signed%20in%20page.png)
        ![Generated invoice page](https://github.com/surba778/greatkart/blob/main/readme-images/Generated%20invoice.png)
        ![Billing form](https://github.com/surba778/greatkart/blob/main/readme-images/billing%20form.png)
        ![Checkout page](https://github.com/surba778/greatkart/blob/main/readme-images/checkout%20page.png)
        ![Orders page](https://github.com/surba778/greatkart/blob/main/readme-images/my%20orders%20page.png)
## Future Prospects 

- Functionality to sort products by rating. 
- Log in and registration via social media account. 
- Functionality to 'save' products to a wishlist. 
- Allow users to delete their account. 
- Custom branded 500 error page would be nice to add in the future.

<br>

# Database

- The SQLite relational DBMS has been used in development to store the data for the project. 
- PostgreSQL relational DBMS has been used in production. 

## Models

- Users
  - User
    - From Django Allauth containing the username, email, and password.
  - UserProfile
    - Model containing the user's details for future reservation.

## Validator Testing
  - [Python validator](http://pep8online.com/)(https://github.com/surba778/greatkart/blob/main/readme-images/testing_results/pep8%20online.png)
  - [HTML Validator](https://validator.w3.org/#validate_by_input)(https://github.com/surba778/greatkart/blob/main/readme-images/testing_results/html_valid.jpg)
  - [CSS Validator](https://jigsaw.w3.org/css-validator/validator)(https://github.com/surba778/greatkart/blob/main/readme-images/testing_results/css%20testing.png)

## Assumptions and Dependencies
Testing is dependent on the website being deployed live on Heroku.

## Access Requirements
Tester must have access to the Django Admin panel in order to manually verify the insertion of records into the databases.

## Regression Testing
Features previously tested during development in a local environment must be regression tested in production on the live website.

## Manual Testing
All user stories have been included in testing along with each model, each test was ticked off the above list when receiving the expected results.

When manually testing paypal payments it was also important to check if the order still completes or not.

When adding, updating or removing events from the cart the quantity and totals updates correctly. After placing an order the quantity of the sold event also updates reducing the quantity available.

A custom 404 page was created for when the user navigates to a link that doesn't exist.

- All Models work correctly.
- All Forms work correctly.
- All Links lead to the correct destinations.
- Quantitys change correctly.
- Items can be removed from the cart correctly.
- Cart quantity updates correctly.
- Default billing in profile can be updated correctly.
- Emails working correctly.
- User profiles can be created.
- Passwords can be reset by email.
- Admin can view admin only pages, and Users cannot access these pages without superuser status.
- Events can be added both front and backend correctly.
- Site responsiveness was tested from mobile, tablet and laptop.
- Site was tested in iOS, Chrome, Safari, and google chrome browser extension for multi browser testing.
- All HTML, CSS, Javascript & Python checked and passed validators.
- All User stories have been completed and tested.

All expected results have passed during manual testing.

# Technologies Used

## Languages 

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

## Libraries & Integrations
- [Django](https://www.djangoproject.com/)
    - Used as the primary framework to build the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to render the forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Used for user authentication on the site.
- [Django Countries](https://pypi.org/project/django-countries/)
    - Used to populate the countries select field on the order form and profile form.
- [Coverage](https://pypi.org/project/coverage/)
    - Used to produce a testing report.
- [Stripe](https://stripe.com/gb)
    - Used to handle payments.
- [Bootstrap](https://getbootstrap.com/)
    - Used as a framework for styling and to make the site responsive via grid system.
- [SQLite](https://www.sqlite.org/index.html)
    - Database used in development.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used in production.
- [Heroku](https://id.heroku.com/login)
    - Online Cloud Platform used to deploy the live site.
- [Gunicorn](https://gunicorn.org/)
    - Used for deploying the project to Heroku.
- [Fontawesome](https://fontawesome.com/)
    - Used for icons across the website. 
- [Google Fonts](https://fonts.google.com/)
    - Used to import "Roboto" & "Mrs Saint Delafield" fonts used across the website. 
- [jQuery](https://jquery.com/)
    - Used to simplify JavaScript code. 
- [Github](https://github.com/)
    - Used to store the project code after being pushed from Git.
- [Git](https://git-scm.com/) 
    - Used for version control to commit to Git and Push to GitHub.

<br>

# Deployment

## Set up project locally

First, ensure the following are set up on your IDE:
- [PIP3](https://pypi.org/project/pip/) Python package installer. 
- [Python 3.8](https://www.python.org/downloads/release/python-360/) or higher.
- [Git](https://git-scm.com/) version control.

To clone the project up locally you can follow the following steps: 

1. Navigate to the repository - [Repository](https://github.com/surba778/greatkart)

2. Click the code dropdown button and copy the url. 

3. Open the terminal in your IDE and enter the following code: 
    - ```
        git clone https://github.com/surba778/greatkart
        ```

4. Install the dependencies needed to run the application by typing the following command into the terminal: 
    - ```
        pip3 install -r requirements.txt
 
5. To set up the database migrate the database models by typing the following commands into the terminal: 
    - ```
        python3 manage.py showmigrations
        python3 manage.py makemigrations
        python3 manage.py migrate
        
6. Create a superuser to have access to the django admin dashboard type the following commands into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 

7. Finally, run the app locally by typing the following command into the terminal: 
    - ```
        python3 manage.py runserver
        ```


## Deploy to Heroku

1. Create a Heroku app: 
    - Go to [Heroku](https://www.heroku.com/) and create an account if you do not have one yet. 
    - From the dashboard click on 'new app' button, name your app and choose the region closest to you. 
    - On the resources tab set up a new Postgres database by searching for 'Postgres'.
2. On your IDE, install 'dj_database_url' & 'psycopg2' to enable the use of the Postgres database: 
    - In the terminal type the following commands:
        - ```
            pip3 install dj_database_url
            pip3 install psycopg2-binary
            ```
3. Add the downloaded dependencies to the requirements file:
    - ```
        pip3 freeze > requirements.txt
        ```
4. To setup the new database go to to settings.py, import 'dj_database_url', comment out the default database configuration and replace the default database with the following: 
    - ```
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse("The URL of your Heroku Postgres database")
        }
        ```
5. Run all migrations to the new Postgres database by entering the following command in the terminal:
    - ```
        python3 manage.py migrate
        ```
6. Create a superuser by typing the following command into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 
7. In settings.py set up the following to use the Postgres database when the app is running on Heroku and the SQLite3 when the app is running locally:
    - ```
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        ```
8. Install Gunicorn (which will act as our webserver) by typing the following commands into the terminal:
    - ```
        pip3 install gunicorn
        pip3 freeze > requirements.txt
        ```
9. Type the following into the procfile: 
    - ```
        web: gunicorn greatkart.wsgi.application
        ```
10. Log in into the Heroku terminal:
    - ```
        heroku login -i
        ```
11. Disable collectstatic to prevent Heroku from collecting static files when deployed, by typing the following command into the terminal: 
    - ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app "heroku_app_name"
        ```
12. In settings.py add the hostname of the Heroku app, and allow localhost: 
    - ```
        ALLOWED_HOSTS = ['"heroku_app_name".herokuapp.com', 'localhost']
        ```
13. Deploy to Heroku by typing the following commands into the terminal: 
    - ```
        heroku git:remote -a "heroku_app_name"
        git push heroku main
        ```
14. To set up automatic deployments in Heroku when pushing code to github:
    - On the deploy tab, connect to github by searching for the repository name and clicking 'Connect'.
    - Click 'Enable Automatic Deploys" 

15. Update the settings.py file to collect the secret key from the environment, and use an empty string as default: 
    - ```
        SECRET_KEY = config('SECRET_KEY')
        ```

# Credits

## Code

- [Code Institute](https://codeinstitute.net/): for git template IDE and heroku deployment instructions.

- [model guidance](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/): This walkthrough help me to set up the model.


## Acknowledgement
- Mentors help and advice
- Tutors help