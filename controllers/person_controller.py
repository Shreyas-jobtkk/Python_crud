# controllers/person_controller.py
from flask import Blueprint
from views.add_person_view import add_person_view
from views.get_person_view import get_person_view
from views.edit_person_view import edit_person_view
from views.delete_person_view import delete_person_view
from views.get_all_persons_view import get_all_persons_view

person_controller = Blueprint('person_controller', __name__)

@person_controller.route('/add_person', methods=['POST'])
def add_person():
    return add_person_view()

@person_controller.route('/get_person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    return get_person_view(person_id)

@person_controller.route('/edit_person/<int:person_id>', methods=['PUT'])
def edit_person(person_id):
    return edit_person_view(person_id)

@person_controller.route('/delete_person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    return delete_person_view(person_id)

@person_controller.route('/get_all_persons', methods=['GET'])
def get_all_persons():
    return get_all_persons_view()
