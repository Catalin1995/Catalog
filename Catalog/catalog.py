import os
from flask import Flask, render_template, json, redirect, request
from mongoengine import connect 
from flask.json import *
from mongoengine import *
from pip._vendor.html5lib.serializer import serialize
from bson import json_util
from bson.objectid import ObjectId

DEBUG = True

db_name = 'tumblelog'

connect(db_name) # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():

    return redirect('/index.html')

# FIXME - remove unsued code, does nothing
@app.route('/students.json', methods = ['GET'])
def get_students():
    return Student2.objects.all().to_json()


@app.route('/students/<id>.json', methods = ['GET'])
def get_students_id(id):
    all_students = Student2.objects
    for student in all_students:
        if str(student.id) == id:
            return student.to_json()

@app.route('/students.json', methods = ['POST'])
def give_students():
    stud = request.get_json()
    student = save_student(stud)
    return student.to_json()


@app.route('/students/<id>.json', methods = ['PATCH'])
def modif_student(id):
    stud = request.get_json()
    modifica_student(id, stud)
    all_students = Student2.objects
    return all_students.to_json()


@app.route('/students/<id>.json', methods=['DELETE'])
def delete_students_id(id):
    delete_student(id)
    all_students = Student2.objects
    return all_students.to_json()


class Student2(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    clasa = StringField(max_length=50)
    data_nasteri = StringField(max_length=50)
    adresa = StringField(max_length=50)
    alte_informati = StringField(max_length=50)


def save_student(stud):
    student = Student2()
    student.first_name = stud['first_name']
    student.last_name = stud['last_name']
    student.clasa = stud['clasa']
    student.data_nasteri = stud['data_nasteri']
    student.adresa = stud['adresa']
    student.alte_informati = stud['alte_informati']
    student.save()
    return student

def modifica_student(id, student):
    for stud in Student2.objects:
        if str(stud.id) == id:
            stud.first_name = student['first_name']
            stud.last_name = student['last_name']
            stud.clasa = student['clasa']
            stud.data_nasteri = student['data_nasteri']
            stud.adresa = student['adresa']
            stud.alte_informati = student['alte_informati']
            stud.save()
            
def delete_student(id):
    for stud in Student2.objects:
        if str(stud.id) == id:
            stud.delete()
            break
    
if __name__ == '__main__':
        
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
