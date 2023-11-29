# views/delete_person_view.py
from flask import jsonify
from models.person_model import PersonModel
from views.person_view import person_deleted_response

person_model = PersonModel()

def delete_person_view(person_id):
    person_model.delete_person(person_id)
    return person_deleted_response()
