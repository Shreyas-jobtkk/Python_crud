# app.py
from flask import Flask
from flask_cors import CORS  # Import CORS
from controllers.person_controller import person_controller

app = Flask(__name__)
CORS(app)

app.register_blueprint(person_controller)

if __name__ == '__main__':
    app.run(debug=True, port=7080)  # Specify the port as 7080