# views/person_view.py
from flask import jsonify

def format_person(person):
    if person:
        return {
            'id': person[0],
            'name': person[1],
            'age': person[2],
            'email': person[3]
        }
    return None

def person_added_response():
    return jsonify({"message": "Person added successfully"})

def person_not_found_response():
    return jsonify({"message": "Person not found"}), 404

def person_updated_response():
    return jsonify({"message": "Person updated successfully"})

def person_deleted_response():
    return jsonify({"message": "Person deleted successfully"})
