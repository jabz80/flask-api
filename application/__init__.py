from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mtjdlzxx:5EBhdg1_kO2X613m554xudbeGvgeUmNu@trumpet.db.elephantsql.com/mtjdlzxx'
db = SQLAlchemy(app)


from application import routes


# the code above sets the connection to PostgreSQL database using SQLAlchemy
# app = Flask(__name__) - creates a flask application instance called app.
# CORS(app) - initializes CORS support for the application
# app.config['SQLALCHEMY_DATABASE_URI'] - sets the database URI for connecting to database.
# db = SQLAlchemy(app) - creates an SQLAlchemy database object db associated with the Flask application app.

# The purpose of this code is to set up a basic Flask web application with support for CORS and a connection to a PostgreSQL database using SQLAlchemy. Once the application is set up, you can define routes and write code in the routes.py file to specify how the application should respond to different HTTP requests (e.g., handling GET and POST requests, rendering templates, etc.). This code is a common starting point for developing web applications with Flask that need database support and cross-origin request handling.