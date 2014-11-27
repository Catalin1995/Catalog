import os
import unittest
import tempfile

import catalog
from catalog import Student

from flask import json


class CatalogTestCase(unittest.TestCase):


    def setUp(self):

        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


    def get_student(self, first_name, last_name, clasa):
        student = {}
        student['first_name'] = first_name
        student['last_name'] = last_name
        student['clasa'] = clasa
        return student


    def test_get_students(self):

        req = self.app.get('/students.json', content_type='application/json')
        students = json.loads(req.data)
        assert students != ""


    def test_create_student(self):

        student = self.get_student("Muresan", "Ionut", "12")
        rv = self.app.post('/students.json',
                           data=json.dumps(student),
                           content_type='application/json')
        data = json.loads(rv.data)
        assert data['first_name'] == "Muresan"
        assert data['last_name'] == "Ionut"
        assert data['clasa'] == "12"


    def test_update_student(self):
        student = Student("First", "Last")
        student.save()
        id = student.id

        student_new = dict(first_name = "Muresan", last_name = "Ionut")
        rv = self.app.patch('/students/'+str(id)+'.json', data = json.dumps(student_new), content_type = 'application/json')
        data = json.loads(rv.data)
        
        for student in data:
            if str(id) == student['_id']['$oid']:
                assert True
                if student['first_name'] == "Muresan":
                    assert True
                else:
                    assert False


    def test_delete_student(self):

        student = Student("First", "Last")
        student.save()
        id = student.id
        
        rv = self.app.delete('/students/'+str(id)+'.json')

        data = json.loads(rv.data)
        for student in data:
            if student['_id']['$oid'] == str(id):
                assert False
        assert True

if __name__ == '__main__':
    unittest.main()
