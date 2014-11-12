import os
from flask import Flask, render_template, json, redirect, request
from mongoengine import connect 

DEBUG = True
connect('tumblelog') # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():
    
    return redirect('/index.html')


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


@app.route('/students/<int:id>.json', methods = ['GET'])
def get_students_id(id):

    #idStud = request.args.get('id', None)
    all_students = studentRepository.return_all_students()
    return json.dumps(all_students[id])


@app.route('/students.json', methods = ['POST'])
def give_students():
    
    #year = request.args.get('year')
    student = Student('Dan','Ciprian', '9-D', '5/5/1555', 'Cluj', 'Telefon: 5555555555')
    studentRepository.add_student(student)
    return json.dumps(student.get_student())

@app.route('/students/:id.json', methods = ['PATCH'])
def modify_student():
    
    id = 1
    student = Student('Maries', 'Alexandru', '10-A', '10/3/1996', '1 Decembrie', 'Telefon: 4444444444')
    stud = student.get_student()
    studentRepository.modify_student(stud, id)
    return json.dumps(stud)
    

@app.route('/students/:id.json', methods=['DELETE'])
def delete_students_id(id = None):
    studentRepository.remove_student_index(2)
    return json.dumps(studentRepository.students)


class Student:  
    
    def __init__(self, first_name, last_name, clasa, data_nasteri, adresa, alte_informati):
    
        self.first_name = first_name
        self.last_name = last_name
        self.clasa = clasa
        self.data_nasteri = data_nasteri
        self.adresa = adresa
        self.alte_informati = alte_informati
        
    def get_student(self):
                
        self.stud = {}
        self.stud['first_name'] = self.first_name
        self.stud['last_name'] = self.last_name
        self.stud['clasa'] = self.clasa
        self.stud['data_nasteri'] = self.data_nasteri
        self.stud['adresa'] = self.adresa
        self.stud['alte_informati'] = self.alte_informati
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

student = Student('Muresan', "Ionut", '12-A', '27/10/1995', 'Dorobantilor 90', 'Telefon: 1111111111')
studentRepository.add_student(student)

student = Student('Dan','Minteuan', '11-B', '10/3/1996', '1 Decembrie', 'Telefon: 2222222222')
studentRepository.add_student(student)

student = Student('Stanciu','Alex', '11-c', '3/11/1990', 'Nasaud 10', 'Telefon: 3333333333')
studentRepository.add_student(student)

if __name__ == '__main__':
        
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
