# controllers/person_controller.py
from flask import Blueprint, request, jsonify
from views.person_view import (
    format_person,
    person_added_response,
    person_not_found_response,
    person_updated_response,
    person_deleted_response
)

from models.person_model import PersonModel

person_controller = Blueprint('person_controller', __name__)
person_model = PersonModel()

@person_controller.route('/add_person', methods=['POST'])
def add_person():
    data = request.get_json()
    name = data['name']
    age = data['age']
    email = data['email']

    person_model.add_person(name, age, email)
    return person_added_response()

@person_controller.route('/get_person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = person_model.get_person(person_id)
    return format_person(person) or person_not_found_response()

@person_controller.route('/edit_person/<int:person_id>', methods=['PUT'])
def edit_person(person_id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    email = data['email']

    person_model.edit_person(person_id, name, age, email)
    return person_updated_response()

@person_controller.route('/delete_person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person_model.delete_person(person_id)
    return person_deleted_response()

@person_controller.route('/get_all_persons', methods=['GET'])
def get_all_persons():
    persons = person_model.get_all_persons()
    formatted_persons = [format_person(person) for person in persons]
    return jsonify(formatted_persons)