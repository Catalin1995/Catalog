import os
from flask import Flask, render_template
from mongoengine import *

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
@app.route('/students.json')
def get_students():
        
    return studentRepository.return_all_students()


@app.route('/students/:id.json')
def get_studentsId():
        
    return studentRepositoryget.get_student_index(index)


@app.route('/students.json')
def give_students():
    student = Student(last_name, first_name)
    studentRepository.add_student(student)


@app.route('/students/:id.json')
def delete_students_id():
        
    remove_student_index(index)


class Student:
        
	def __init__(self, first_name, last_name):
                
		self.first_name = first_name
		self.last_name = last_name


	def get_student(self):
                
		self.stud = {}
		self.stud['first_name'] = self.first_name
		self.stud['last_name'] = self.last_name
		return (self.stud)


	def all(self):
                
		return []


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


studentRepository = StudentRepository()

student = Student('ionut','muresan')
studentRepository.add_student(student)

student = Student('dan','minteuan')
studentRepository.add_student(student)

student = Student('catalin','jon')
studentRepository.add_student(student)


if __name__ == '__main__':
        
	port = int(os.environ.get("PORT", 1337))
	app.run(host='0.0.0.0', port=port)
	app.run()
