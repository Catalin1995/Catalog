import os
import catalog
import unittest
import tempfile

from flask import json


class CatalogTestCase(unittest.TestCase):


    def setUp(self):

        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


    def test_get_students(self):

        req = self.app.get('/students.json', content_type='application/json')
        students = json.loads(req.data)
        print(students)


    def test_create_student(self):

        pass


    def test_update_student(self):

        pass


    def test_delete_student(self):

        pass


if __name__ == '__main__':
    unittest.main()
