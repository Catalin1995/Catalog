import catalog
import os
import unittest
from catalog import Student

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


class catalogTestCase(unittest.TestCase):
    def test_sum(self):
        assert 1+1 == 2
        student = {}

    def test_studentRoot(self):
        first_name = "Muresan"
        last_name = "Ionut"
        student = Student(first_name, last_name)
        assert student.first_name == "Muresan"
        assert student.last_name == "Ionut" 

if (__name__ == '__main__'):
    unittest.main()
