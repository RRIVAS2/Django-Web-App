# Overview

BeBetter is an app that allows users to manually enter the time they waste in social media or doom scrolling. The purpose of this app is to allow users to be mindful of how they use their time.

In order to run this app, you need to install Django on your computer. You can follow this instructions to get it installed: https://docs.djangoproject.com/en/6.0/intro/install/

How to run the projects+:

How to Run the Project:

1. Prerequisites & Installation:
   Make sure Python is installed. Clone this repository, set up a virtual environment, and install Django (You can follow this instructions to get it installed: https://docs.djangoproject.com/en/6.0/intro/install/):

Bash
python -m venv djangoenv

# On Windows:

.\djangoenv\Scripts\activate

# On Mac/Linux:

source djangoenv/bin/activate

pip install django

2. Run Migrations:
   Ensure the local SQLite database tables are generated:

Bash
python manage.py migrate

3. Start the Development Server:

Bash
python manage.py runserver

4. Access the App:
   Open your web browser and navigate to:
   http://127.0.0.1:8000/

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

The Home page guest view displays a welcome screen explaining the app's purpose and prompting visitors to Log In or Sign Up.
Once users are logged in, the authenticated view is display. This new page includs a form where the user loggs their time, and a table that displays all the users logs.

There are also authentication pages. These pages can be accesed through links in the guest page, or from the navigation bar.

The web page has some interactive information based on the user. A welcome message with the user name is displayed when the user logs in. Also, a table populated with user logs is dinamycally populated when the user enters a new log.

# Development Environment

Framework: Django 6.0.7
Language: Python 3.13.7
Database: SQLite (default local relational storage managed via Django ORM)
Authentication: django.contrib.auth

# Useful Websites

- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
- [Django Official Website](https://www.djangoproject.com/start/)

# Future Work

- Polish the front end, improve UX
- Add more functionalities with the purpose of helping users make a better use of their, for example: prompting users to add their interests/hobbies, and allow them to track the time they use on those activities.
- Add AI functionality that recommends productive activities based on user interests.
