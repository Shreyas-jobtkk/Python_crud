# views/edit_person_view.py
from flask import request, jsonify
from models.person_model import PersonModel
from views.person_view import person_updated_response

person_model = PersonModel()

def edit_person_view(person_id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    email = data['email']

    person_model.edit_person(person_id, name, age, email)
    return person_updated_response()
