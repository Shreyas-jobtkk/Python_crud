# models/person_model.py
import psycopg2

class PersonModel:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='postgres', user='postgres', password='mysecretpassword', host='localhost', port='5432')
        self.cursor = self.connection.cursor()

        # Create schema if not exists
        self.cursor.execute('CREATE SCHEMA IF NOT EXISTS crud;')
        self.connection.commit()

        # Create table if not exists in the "crud" schema
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS crud.person (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                email VARCHAR(100) NOT NULL
            );
        ''')
        self.connection.commit()

    def add_person(self, name, age, email):
        self.cursor.execute('INSERT INTO crud.person (name, age, email) VALUES (%s, %s, %s)', (name, age, email))
        self.connection.commit()

    def get_person(self, person_id):
        self.cursor.execute('SELECT * FROM crud.person WHERE id = %s', (person_id,))
        return self.cursor.fetchone()

    def edit_person(self, person_id, name, age, email):
        self.cursor.execute('UPDATE crud.person SET name=%s, age=%s, email=%s WHERE id=%s', (name, age, email, person_id))
        self.connection.commit()

    def delete_person(self, person_id):
        self.cursor.execute('DELETE FROM crud.person WHERE id = %s', (person_id,))
        self.connection.commit()

    def get_all_persons(self):
        self.cursor.execute('SELECT * FROM crud.person')
        return self.cursor.fetchall()