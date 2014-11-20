import os
from flask import Flask, render_template, json, redirect, request
from mongoengine import connect 
from flask.json import *
from mongoengine import *
from pip._vendor.html5lib.serializer import serialize
from bson import json_util
from bson.objectid import ObjectId
from module.modifStudent import modifica_student, delete_student, save_student

DEBUG = True

db_name = 'tumblelog'

connect(db_name)  # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():

    return redirect('/index.html')

# FIXME - remove unsued code, does nothing
@app.route('/students.json', methods=['GET'])
def get_students():
    return Student.objects.all().to_json()


@app.route('/students/<id>.json', methods=['GET'])
def get_students_id(id):
    all_students = Student.objects
    for student in all_students:
        if str(student.id) == id:
            return student.to_json()

@app.route('/students.json', methods=['POST'])
def give_students():
    stud = request.get_json()
    student = Student(stud)
    return student.to_json()


@app.route('/students/<id>.json', methods=['PATCH'])
def modif_student(id):
    stud = request.get_json()
    modifica_student(id, stud, Student.objects)
    all_students = Student.objects
    return all_students.to_json()


@app.route('/students/<id>.json', methods=['DELETE'])
def delete_students_id(id):
    print(id)
    delete_student(id, Student.objects)
    all_students = Student.objects
    return all_students.to_json()


class Student(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    clasa = StringField(max_length=50)
    data_nasteri = StringField(max_length=50)
    adresa = StringField(max_length=50)
    alte_informati = StringField(max_length=50)
    
    def modifica_student(id, student, all_students):
        for stud in all_students:
            if str(stud.id) == id:
                stud.first_name = student['first_name']
                stud.last_name = student['last_name']
                stud.clasa = student['clasa']
                stud.data_nasteri = student['data_nasteri']
                stud.adresa = student['adresa']
                stud.alte_informati = student['alte_informati']
                stud.save()
            
    def delete_student(id, all_students):
        for stud in all_students:
            if str(stud.id) == id:
                stud.delete()
                break

    
if __name__ == '__main__':
        
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
