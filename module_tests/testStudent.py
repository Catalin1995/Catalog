import catalog
import os
import pep8
import unittest
from catalog import Student, StudentRepository
from catalog import Student2

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
    
    def test_student2_class(self):
        student = Student2()
        student.first_name = "Muresan"
        student.last_name = "Ionut"
        student.clasa = "12-A"
        student.data_nasteri = "27/10/1995"
        student.adresa = "Dorobantilor 90"
        student.alte_informati = "Telefon: 1"
        dimension = len(Student2.objects)
        student.save()
        assert len(Student2.objects) == dimension+1
        student.delete()
        
        student = Student2()
        student.first_name = "Dan"
        student.last_name = "Minteuan"
        student.clasa = "10-C"
        student.data_nasteri = "11/04/2000"
        student.adresa = "Nasaud 19"
        student.alte_informati = "Telefon: 2"
        dimension = len(Student2.objects) 
        student.save()
        assert len(Student2.objects) == dimension+1
        
        student.delete()
        nume = Student2.objects(first_name="Muresan").count()
        print("nume= ",nume)
        
if (__name__ == '__main__'):
    unittest.main()
