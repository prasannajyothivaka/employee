from sqlalchemy.orm import validates
from app import db

import json


class Employee1(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lname = db.Column(db.String(50))

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "lname": self.lname,
        }

    def add_employee(data):
        #import pdb; pdb.set_trace()
        employee = Employee1(name=data['name'], lname=data['lname'])
        db.session.add(employee)
        db.session.commit()
    
    def get_employee( id):
        return Employee1.json(Employee1.query.get(id))

    def get_all_employees():
        #import pdb; pdb.set_trace()
        return [employee.json() for employee in Employee1.query.all()]
    
    def update_employee(id, name=None, lname=None):
        #import pdb; pdb.set_trace()
        employee = Employee1.query.get(id)
        employee.name  = name or employee.name 
        employee.lname = lname or employee.lname 
        db.session.commit()
    

    def delete_employee(id):
        #import pdb; pdb.set_trace()
        data = Employee1.query.get(id)
        db.session.delete(data)
        db.session.commit()

if __name__ == "__main__":
    db.create_all()
