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
        
        student = {}
        student["first_name"] = 'Muresan'
        student['last_name'] = 'Ionut'
        student['clasa'] = '12-A'
        student['data_nasteri'] = '11/11/1111'
        student['adresa'] = 'Dorobantilor 90'
        student['alte_informati'] = 'telefon: 1104823'
        student = Student(student)
        assert student.first_name == "Muresan"
        assert student.last_name == "Ionut" 
        assert student.clasa == "12-A" 
        assert student.data_nasteri == "11/11/1111" 
        assert student.adresa == "Dorobantilor 90" 
        assert student.alte_informati == "telefon: 1104823"


    def test_dict_student(self):

        student = {}
        student["first_name"] = 'Muresan'
        student['last_name'] = 'Ionut'
        student['clasa'] = '12-A'
        student['data_nasteri'] = '11/11/1111'
        student['adresa'] = 'Dorobantilor 90'
        student['alte_informati'] = 'telefon: 1104823'
        
        student = Student(student)
        stud = student.dict_student()
        
        assert stud['first_name'] == "Muresan"
        assert stud['last_name'] == "Ionut" 
        assert stud['clasa'] == "12-A" 
        assert stud['data_nasteri'] == "11/11/1111" 
        assert stud['adresa'] == "Dorobantilor 90" 
        assert stud['alte_informati'] == "telefon: 1104823"
#         stud = student.get_student()
#         assert stud['first_name'] == 'Muresan'
#         assert stud['last_name'] == 'Ionut' 
# 
#         first_name = 'Minteuan'
#         last_name = 'Dan'
#         student = Student(first_name, last_name)
#         stud = student.get_student()
#         assert stud['first_name'] == 'Minteuan'
#         assert stud['last_name'] == 'Dan'


if (__name__ == '__main__'):
    unittest.main()
