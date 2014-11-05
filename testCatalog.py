import catalog
import os
import unittest
from catalog import Student

class catalogTestCase(unittest.TestCase):
    #def __init__():
        
    def test_sum(self):
        assert 1+1 == 2
        student = {}

    def test_studentRoot(self):
        nume = "Muresan"
        prenume = "Ionut"
        clasa = "12-A"
        student = Student(nume, prenume, clasa)
        assert student.nume == "Muresan"
        assert student.prenume == "Ionut"
        assert student.clasa == "12-A"   

if (__name__ == '__main__'):
    unittest.main()
#qasd
