# views/get_person_view.py
from flask import jsonify
from models.person_model import PersonModel
from views.person_view import format_person, person_not_found_response

person_model = PersonModel()

def get_person_view(person_id):
    person = person_model.get_person(person_id)
    return format_person(person) or person_not_found_response()
