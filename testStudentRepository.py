import catalog
import os
import unittest
from catalog import Student, StudentRepository

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()
        
class StudentRepositoryTestCase(unittest.TestCase):

    def test_addStudent(self):
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.addStudent(student)
        assert studentRepository.students[0]['first_name'] == 'Muresan'
        assert studentRepository.students[0]['last_name'] == 'Ionut'

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)
        assert studentRepository.students[1]['first_name'] == 'Dan'
        assert studentRepository.students[1]['last_name'] == 'Minteuan'


    def test_returnAllStudents(self):
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.addStudent(student)

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)
        students = studentRepository.returnAllStudents()
        
        assert students[0]['last_name'] == 'Ionut'
        assert students[0]['first_name'] == 'Muresan'
        assert students[1]['last_name'] == 'Minteuan'
        assert students[1]['first_name'] == 'Dan'

    def test_removeStudentIndex(self):
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.addStudent(student)

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)

        first_name = "Muresan"
        last_name = "Cosmin"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)
        
        studentRepository.removeStudentIndex(1)
        assert studentRepository.students[0]['last_name'] == 'Ionut'
        assert studentRepository.students[0]['first_name'] == 'Muresan'
        assert studentRepository.students[1]['last_name'] == 'Cosmin'
        assert studentRepository.students[1]['first_name'] == 'Muresan'

        studentRepository.removeStudentIndex(0)
        assert studentRepository.students[0]['last_name'] == 'Cosmin'
        assert studentRepository.students[0]['first_name'] == 'Muresan'

        studentRepository.removeStudentIndex(0)
        assert studentRepository.students == []

    def test_getStudentIndex(self):
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.addStudent(student)

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)

        first_name = "Muresan"
        last_name = "Cosmin"
        student = Student(first_name, last_name)
        studentRepository.addStudent(student)
        
        assert studentRepository.getStudentIndex(0) == {'first_name': 'Muresan', 'last_name': 'Ionut'}
        assert studentRepository.getStudentIndex(1) == {'first_name': 'Dan', 'last_name': 'Minteuan'}
        assert studentRepository.getStudentIndex(2) == {'last_name': 'Cosmin', 'first_name': 'Muresan'}
if (__name__ == '__main__'):
    unittest.main()
