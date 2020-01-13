# Project 3

[Click to view how it works on Youtube](https://www.youtube.com/watch?v=eqpwtkJV6W4&list=PLN7IjqCA_0yBy38bWpZo7b30hZYx6f5dS&index=5&t=0s)

Web Programming with Python and JavaScript

Project Author: Isaac Newton Kissiedu

This project is a Django web app for Pizza Orders, Checkout and Admin Backend for managing prices and data.

The project relies on HTML, CSS,Bootstrap Framework, Python, Django and Sqlite database for relational database managment.

**FILES IN THE PROJECT**

1. **manage.py:**

This file provides API for the Django framework project management

2. **templates:** 

This is a folder that contains all html files available to the entire site.

3. **static:** 

This is a folder that contains all the images, javascript and stylesheets available to the entire site.

4. **db.sqlite3:** 

This is a sqlite relational database used by the application for data storage

5. **users:** 

This is a django app used to implement Registration,Login and Logout features

6. **pizza:** 

This is the django project directory which contains the site settings and root urls

7. **orders:** 

This is a django app to implement Orders,Add to cart, Empty Cart, Remove Cart Item, Preview Checkout, Process Order and My Orders features.

**HOW TO RUN THE APP**

Create a Python 3 virtual environment and activate it.

Install the python packages available in requirements.txt

Run the application by using the following command: `$ python3 manage.py runserver`