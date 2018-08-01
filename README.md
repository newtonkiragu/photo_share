# Photo Share
An image sharing social media application.

## Description
Photo Share is a social web application that allows users to post images and view images posted by other users. Users can follow other users to view their pictures when posted.  Users can allows use the search feature and explore images posted by people that they do not follow.

Features
* Users create an account 
* Users are required to verify their email address before logging in.
* Users can view other users profile pages.
* Image details of images on profile page are displayed on a modal.
* Logged in users.
* Logged in users can follow and unfollow other user accounts.
* Logged in users can like an image (only once).
* Logged in user can comment on an image multiple times
* Lgged in users can edit their profile.

Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

Technologies Used
* Backend
  * Python 3.6.5
  * Django 2.0
* Front End
  * HTML, CSS and Bootstrap
  * JavaScript
* Database
  * Postgressql
* Deployment
  * Heroku
  

### Requirements
Python3.6
Postgres
Python virtualenv

### Setup and installation
Clone the Repo
Create a virtual environment in the root folder using python3.6 as default handler
```bash
python3 -m virtualenv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```    

Install the project dependencies
```bash
pip3 install -r requirements.txt
```

Create a postgres database.


Create .env file and paste paste the following filling where appropriate:
```bash
touch .env
```

SECRET_KEY = '<Secret_key>'

DBNAME = 'instagramdb'

USER = '<Username>'

PASSWORD = '<password>'

DEBUG = True

Run initial Migration

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Running the server 
```bash
python manage.py runserver
```

View the application on your browser on localhost:8000

## Known bugs
No known bugs so far. Create an issue on the repository.

## [LICENSE](LICENSE)
This project is licensed under the MIT Open Source license, (c) [Adiela Abishua](https://github.com/adiela)