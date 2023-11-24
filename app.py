# app.py
from flask import Flask
from controllers.person_controller import person_controller

app = Flask(__name__)

app.register_blueprint(person_controller)

if __name__ == '__main__':
    app.run(debug=True)
