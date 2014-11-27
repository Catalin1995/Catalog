'''
Created on Nov 26, 2014

@author: ionut.muresan
'''
import os
from flask import Flask, render_template, json, redirect, request
from mongoengine import connect
from flask.json import *
from mongoengine import *
from pip._vendor.html5lib.serializer import serialize
from bson import json_util
from bson.objectid import ObjectId
import catalog
from catalog.student import *


DEBUG = True

db_name = 'tumblelog'

connect(db_name)  # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)


@app.route('/')
def index():

    return redirect('/index.html')


@app.route('/students.json', methods=['GET'])
def get_students():

    return Student.objects.all().to_json()


@app.route('/students/<id>.json', methods=['GET'])
def get_students_id(id):
    print(id)
    all_students = Student.objects
    for student in all_students:
        if str(student.id) == id:
            print("asd")
            return student.to_json()


@app.route('/students.json', methods=['POST'])
def give_students():

    stud = request.get_json()
    student = Student(**stud)
    student.save()
    return student.to_json()


@app.route('/students/<id>.json', methods=['PATCH'])
def modif_student(id):

    stud = request.get_json()
    new_student = Student(**stud)
    student = Student.objects.get(id=id)
    student.update_student(new_student)
    student.save()
    return Student.objects.to_json()


@app.route('/students/<id>.json', methods=['DELETE'])
def delete_students_id(id):

    student = Student.objects.get(id=id)
    student.delete()
    all_students = Student.objects
    return all_students.to_json()

    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
