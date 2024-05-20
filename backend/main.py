# Author(s): Yee Chuen teoh
'''
Note:
    - main endpoint

Usage:
    python main.py
'''
# imports
from flask import request, jsonify
from config import app, db
from models import Contact

# endpoints
# GET endpoint (read)
@app.route("/contacts", methods = ["GET"]) # <-- this is a decorator that goes above a function
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}), 200 # <-- by default return 200 (success)

# POST endpoint (create)
@app.route("/create_contact", methods = ["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "Must include first name, last name and email"}), 400

    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)

    # attempt to add to db
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400    
    
    return jsonify({"message": "Contact created"}), 201

# PATCH/PUT endpoint (update)
@app.route("/update_contact/<int:contact_id>", methods = ["PATCH"])
def update_contact(contact_id): # <-- parameter specify need to be the same as flask endpoint. <int:<param>>
    contact = Contact.query.get(contact_id)

    if not contact:
        return jsonify({"message": "Contact not found"})
    
    data = request.json
    # data.get(key, default)
    # it looks for key, and return the value
    # if key don't exist, return the default value
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "Contact updated"}), 200

# DELETE endpoint (delete)
@app.route("/delete_contact/<int:contact_id>", methods = ["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)

    if not contact:
        return jsonify({"message": "Contact not found"})
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact deleted"}), 200

# main
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug = True)
