# views/get_all_persons_view.py
from flask import jsonify
from models.person_model import PersonModel
from views.person_view import format_person

person_model = PersonModel()

def get_all_persons_view():
    persons = person_model.get_all_persons()
    formatted_persons = [format_person(person) for person in persons]
    return jsonify(formatted_persons)
