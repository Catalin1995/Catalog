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


class Student:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def getStudent(self):
		self.stud = {}
		self.stud['first_name'] = self.first_name
		self.stud['last_name'] = self.last_name
		return (self.stud)

	def all(self):
		return []

class StudentRepository:
        def __init__(self):
                self.students = []
                
        def addStudent(self, student):
                self.students.append(student.getStudent())
                
        def returnAllStudents(self):
                return (self.students)
        
        def removeStudentIndex(self, index):
                del(self.students[index])

        def getStudentIndex(self, index):
                return self.students[index]

            
student = Student('ionut','muresan')
studentRepository = StudentRepository()
studentRepository.addStudent(student)
student = Student('dan','minteuan')
studentRepository.addStudent(student)
student = Student('catalin','jon')
studentRepository.addStudent(student)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 1337))
	app.run(host='0.0.0.0', port=port)
	app.run()
 
