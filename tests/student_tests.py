import os
import pep8
import unittest
import catalog
from catalog.catalog import Student
from catalog.catalog import *

class BaseTestCase(unittest.TestCase):
 
    def setUp(self):
 
        catalog.catalog.app.config['TESTING'] = True
        self.app = catalog.catalog.app.test_client()


class StudentTestCase(unittest.TestCase):

    def test_Student_class(self):
        student = Student()
        student.first_name = "Muresan"
        student.last_name = "Ionut"
        student.clasa = "12-A"
        student.data_nasteri = "27/10/1995"
        student.adresa = "Dorobantilor 90"
        student.alte_informati = "Telefon: 1"
        student.note = ['2','3','4','5']
        student.absente = ['10/10/2010', '20/20/2010', '30/30/2030']
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
        student.note = ['2','3','10']
        student.absente = ['10/20/3000', '20/30/1000']
        dimension = len(Student.objects)
        student.save()
        assert len(Student.objects) == dimension+1
 
        student.delete()
        nume = Student.objects(first_name="Muresan").count()

    def test_update_student(self):
        note = ['2','3','4','5']
        absente = ['10/10/2010', '20/20/2010', '30/30/2030']
        oldStud = Student('muresan', 'ionut', '12-A',
                          '27/10/1995', 'Dorobantilor 90', 'Telefon: 1',
                          note, 
                          absente)
        newStud = {}
        newStud['first_name'] = 'dan'
        newStud['last_name'] = 'minteuan'
        newStud['clasa'] = '11-A'
        newStud['data_nasteri'] = '11/11/1111'
        newStud['adresa'] = 'Dorobantilor 1'
        newStud['alte_informati'] = 'Telefon: 2'
        newStud['note'] = ['2','3','4','5']
        newStud['absente'] = ['10/10/2010', '20/20/2010', '30/30/2030']
         
        oldStud.update_student(newStud)
         
        assert oldStud.first_name == 'dan'
        assert oldStud.last_name == 'minteuan'
        assert oldStud.clasa == '11-A'
        assert oldStud.data_nasteri == '11/11/1111'
        assert oldStud.adresa == 'Dorobantilor 1'
        assert oldStud.alte_informati == 'Telefon: 2'
        assert oldStud.note == ['2', '3', '4', '5']
        assert oldStud.absente == ['10/10/2010', '20/20/2010', '30/30/2030']


if (__name__ == '__main__'):
    unittest.main()