import json
import os

DATABASE_FILE = 'animal_xrays_db.json'

def read_database():
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, 'r') as file:
        return json.load(file)

def write_database(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
