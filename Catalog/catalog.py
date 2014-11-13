import os
from flask import Flask, render_template, json, redirect, request
from mongoengine import connect 
from flask.json import jsonify

DEBUG = True
connect('tumblelog') # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():

    return redirect('/index.html')

# FIXME - remove unsued code, does nothing
@app.route('/students.json', methods = ['GET'])
def get_students():
    
    all_students = studentRepository.return_all_students()
    return json.dumps(all_students)


@app.route('/students/<id>.json', methods = ['GET'])
def get_students_id(id):

    id = int(id)
    all_students = studentRepository.return_all_students()
    if id>len(all_students)-1:
        error = {}
        error['Id'] = 'Id-ul este prea mare'
        return json.dumps(error)
    if id<0:
        error = {}
        error['Id'] = 'Id-ul este prea mic'
        return json.dumps(error)
    return json.dumps(all_students[id])


@app.route('/students.json', methods = ['POST'])
def give_students():
    stud = request.get_json()
    student = Student(stud)
    studentRepository.add_student(student)
    return json.dumps(student.dict_student())

@app.route('/students/<id>.json', methods = ['PATCH'])
def modify_student(id):
    id = int(id)
    stud = request.get_json()
    student = Student(stud)
    studentRepository.modify_student(student, id)
    all_students = studentRepository.return_all_students()
    return json.dumps(all_students)


@app.route('/students/<id>.json', methods=['DELETE'])
def delete_students_id(id):
    
    id = int(id)
    studentRepository.remove_student_index(id)
    return json.dumps(studentRepository.students)
    

class Student:  
    
    def __init__(self, data):
         
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.clasa = data['clasa']
        self.data_nasteri = data['data_nasteri']
        self.adresa = data['adresa']
        self.alte_informati = data['alte_informati']

    def dict_student(self):
                
        self.stud = {}
        self.stud['first_name'] = self.first_name
        self.stud['last_name'] = self.last_name
        self.stud['clasa'] = self.clasa
        self.stud['data_nasteri'] = self.data_nasteri
        self.stud['adresa'] = self.adresa
        self.stud['alte_informati'] = self.alte_informati
        print(self.stud)
        return self.stud


class StudentRepository:
        
    def __init__(self):
   
        self.students = []

                
    def add_student(self, student):

        self.students.append(student.dict_student())

                
    def return_all_students(self):
       
        return (self.students)


    def remove_student_index(self, index):
          
        del(self.students[index])


    def get_student_index(self, index):
                
        return self.students[index]
    
    
    def modify_student(self, student, id):
            
        self.students[id]  = student


studentRepository = StudentRepository()
data = {}
data['first_name'] = 'Muresan'
data['last_name'] = 'Ionut'
data['clasa'] = '12-A'
data['data_nasteri'] = '27/10/1995'
data['adresa'] = 'Dorobantilor 90'
data['alte_informati'] = 'Telefon: 1111111111'
student = Student(data)
studentRepository.add_student(student)

data['first_name'] = 'Muresan'
data['last_name'] = 'Traian'
data['clasa'] = '11-B'
data['data_nasteri'] = '11/04/1995'
data['adresa'] = 'Dorobantilor 90'
data['alte_informati'] = 'Telefon: 2222222222'
student = Student(data)
studentRepository.add_student(student)

data['first_name'] = 'Comsa'
data['last_name'] = 'Andreea'
data['clasa'] = '10-C'
data['data_nasteri'] = '06/10/1990'
data['adresa'] = 'Nasaud 10'
data['alte_informati'] = 'Telefon: 3333333333'
student = Student(data)
studentRepository.add_student(student)

if __name__ == '__main__':
        
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
