from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database2.sqlite3"

db = SQLAlchemy(app)

from models import *

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"data": Employee1.get_all_employees()})

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    return jsonify(Employee1.get_employee(id=id))

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    Employee1.add_employee(data)
    return Response("Employee added", 201, mimetype='application/json')

@app.route('/employee', methods=['PUT'])
def update_employee():
    data = request.get_json()
    Employee1.update_employee(**data)
    return Response("Employee Updated", status=200, mimetype='application/json')

@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    Employee1.delete_employee(id=id)
    return Response("employee Deleted", status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run()