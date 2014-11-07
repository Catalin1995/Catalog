import catalog
import os
import unittest
from catalog import Student, StudentRepository

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


class StudentRepositoryTestCase(unittest.TestCase):

    def test_add_student(self):

        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.add_student(student)
        assert studentRepository.students[0]['first_name'] == 'Muresan'
        assert studentRepository.students[0]['last_name'] == 'Ionut'

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)
        assert studentRepository.students[1]['first_name'] == 'Dan'
        assert studentRepository.students[1]['last_name'] == 'Minteuan'


    def test_return_all_students(self):

        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.add_student(student)
        
        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)
        students = studentRepository.return_all_students()


        assert students[0]['last_name'] == 'Ionut'
        assert students[0]['first_name'] == 'Muresan'
        assert students[1]['last_name'] == 'Minteuan'
        assert students[1]['first_name'] == 'Dan'


    def test_remove_student_index(self):

        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.add_student(student)

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)

        first_name = "Muresan"
        last_name = "Cosmin"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)
        
        studentRepository.remove_student_index(1)
        assert studentRepository.students[0]['last_name'] == 'Ionut'
        assert studentRepository.students[0]['first_name'] == 'Muresan'
        assert studentRepository.students[1]['last_name'] == 'Cosmin'
        assert studentRepository.students[1]['first_name'] == 'Muresan'

        studentRepository.remove_student_index(0)
        assert studentRepository.students[0]['last_name'] == 'Cosmin'
        assert studentRepository.students[0]['first_name'] == 'Muresan'

        studentRepository.remove_student_index(0)
        assert studentRepository.students == []


    def test_get_student_index(self):
        
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        studentRepository = StudentRepository()
        studentRepository.add_student(student)

        first_name = "Dan"
        last_name = "Minteuan"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)

        first_name = "Muresan"
        last_name = "Cosmin"
        student = Student(first_name, last_name)
        studentRepository.add_student(student)

        assert studentRepository.get_student_index(0) == {'first_name': 'Muresan', 'last_name': 'Ionut'}
        assert studentRepository.get_student_index(1) == {'first_name': 'Dan', 'last_name': 'Minteuan'}
        assert studentRepository.get_student_index(2) == {'last_name': 'Cosmin', 'first_name': 'Muresan'}


if (__name__ == '__main__'):
    unittest.main()
