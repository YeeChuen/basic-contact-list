# Author(s): Yee Chuen teoh
'''
Note:
    - contain database model
    - here is where you create class

Usage:

'''

# imports
from config import db # <-- the db instance created in config.py

# class
class Contact(db.Model):
    # below is similar to creating table in SQL
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique = False, nullable = False) # 80 is the max character
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    def to_json(self):
        # camelCase due JS naming convention
        # snake-case is Python naming convention
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
    
