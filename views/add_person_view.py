# views/add_person_view.py
from flask import request, jsonify
from models.person_model import PersonModel
from views.person_view import person_added_response

person_model = PersonModel()

def add_person_view():
    data = request.get_json()
    name = data['name']
    age = data['age']
    email = data['email']

    person_model.add_person(name, age, email)
    return person_added_response()
