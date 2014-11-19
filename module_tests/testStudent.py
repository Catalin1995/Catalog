import catalog
import os
import pep8
import unittest
from catalog import Student

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):

        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


class StudentTestCase(unittest.TestCase):
    
    def test_Student_class(self):
        student = Student()
        student.first_name = "Muresan"
        student.last_name = "Ionut"
        student.clasa = "12-A"
        student.data_nasteri = "27/10/1995"
        student.adresa = "Dorobantilor 90"
        student.alte_informati = "Telefon: 1"
        dimension = len(Student.objects)
        student.save()
        assert len(Student.objects) == dimension+1
        student.delete()
        
        student = Student()
        student.first_name = "Dan"
        student.last_name = "Minteuan"
        student.clasa = "10-C"
        student.data_nasteri = "11/04/2000"
        student.adresa = "Nasaud 19"
        student.alte_informati = "Telefon: 2"
        dimension = len(Student.objects) 
        student.save()
        assert len(Student.objects) == dimension+1
        
        student.delete()
        nume = Student.objects(first_name="Muresan").count()
        print("nume= ",nume)
        
if (__name__ == '__main__'):
    unittest.main()
