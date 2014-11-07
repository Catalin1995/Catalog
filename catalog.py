import os
from flask import Flask, render_template, json
from mongoengine import *
#from flask.json import jsonify

DEBUG = True
connect('tumblelog') # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():
        
	return render_template('index.html')


@app.route('/clasa.html')
def clasa(name = "Class Page"):
        
	return render_template('clasa.html')


@app.route('/clase.html')
def clase(name = "Clase Page"):
        
	return render_template('clase.html')


@app.route('/elev.html')
def elev(name = "Elev Page"):
        
	return render_template('elev.html',)


# FIXME - remove unsued code, does nothing
@app.route('/students.json', methods = ['GET'])
def get_students():
    
    all_students = studentRepository.return_all_students()
    return json.dumps(all_students)


@app.route('/students/:id.json', methods = ['GET'])
def get_students_id(id=None):

    all_students = studentRepository.return_all_students()
    return json.dumps(all_students[0])


@app.route('/students.json', methods = ['POST'])
def give_students():
    
    student = Student('alex','stanciu')
    studentRepository.add_student(student)
    return json.dumps(student.get_student())

@app.route('/students/:id.json', methods = ['PATCH'])
def modify_student():
    
    id = 1
    firt_name = 'Maries'
    last_name = 'Alexandru'
    student = Student('maries', 'alexandru')
    stud = student.get_student()
    studentRepository.modify_student(stud, id)
    return json.dumps(stud)
    

@app.route('/students/:id.json', methods=['DELETE'])
def delete_students_id(id = None):
    studentRepository.remove_student_index(2)
    return json.dumps(studentRepository.students)


class Student:
        
	def __init__(self, first_name, last_name):
    
		self.first_name = first_name
		self.last_name = last_name
        
	def get_student(self):
                
		self.stud = {}
		self.stud['first_name'] = self.first_name
		self.stud['last_name'] = self.last_name
		return (self.stud)


class StudentRepository:
        
    def __init__(self):
   
        self.students = []

                
    def add_student(self, student):

        self.students.append(student.get_student())
     
                
    def return_all_students(self):
       
        return (self.students)


    def remove_student_index(self, index):
          
        del(self.students[index])


    def get_student_index(self, index):
                
        return self.students[index]
            
    def modify_student(self, student, id):
            
         self.students[id]  = student


studentRepository = StudentRepository()

student = Student('Ionut','Muresan')
studentRepository.add_student(student)

student = Student('Dan','Minteuan')
studentRepository.add_student(student)

student = Student('Catalin','Jon')
studentRepository.add_student(student)

if __name__ == '__main__':
        
	port = int(os.environ.get("PORT", 1337))
	app.run(host='0.0.0.0', port=port)
	app.run()
