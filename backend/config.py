# Author(s): Yee Chuen teoh
'''
Note:
    - configurations here, initialization, db instance.

Usage:

'''
# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# main
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # <-- we're not going to track all changes made to the db.

db = SQLAlchemy(app) # <-- create a db instance to allow CRUD operation
