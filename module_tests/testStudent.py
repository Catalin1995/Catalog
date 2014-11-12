import catalog
import os
import pep8
import unittest
from catalog import Student, StudentRepository

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):

        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


class StudentTestCase(unittest.TestCase):

    # FIXME coding style - method name
    # think of a better name
    def test_student_class(self):
        
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        assert student.first_name == "Muresan"
        assert student.last_name == "Ionut" 


    def test_get_student(self):

        first_name = 'Muresan'
        last_name = 'Ionut'
        student = Student(first_name, last_name)
        stud = student.get_student()
        assert stud['first_name'] == 'Muresan'
        assert stud['last_name'] == 'Ionut' 

        first_name = 'Minteuan'
        last_name = 'Dan'
        student = Student(first_name, last_name)
        stud = student.get_student()
        assert stud['first_name'] == 'Minteuan'
        assert stud['last_name'] == 'Dan'


print("Found %s errors (and warnings)" % file_errors)
if (__name__ == '__main__'):
    unittest.main()
