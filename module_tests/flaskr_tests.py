import os
import pep8
import catalog
import unittest
import tempfile
from flask import json


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


    def test_get_student_id(self):
        
        rv = self.app.get('/students/:id.json')
        data = json.loads(rv.data)
        assert data['first_name'] == 'Ionut'
        assert data['last_name'] == 'Muresan'
        
        
    def test_get_students(self):
        
        rv = self.app.get('/students.json')
        data = json.loads(rv.data)
        assert data[0]['last_name'] == 'Muresan'
        assert data[0]['first_name'] == 'Ionut'
        assert data[1]['last_name'] == 'Minteuan'
        assert data[1]['first_name'] == 'Dan'
        #assert data[2]['last_name'] == 'jon'
        #assert data[2]['first_name'] == 'catalin'
    
        
    def test_give_students(self):
        
        rv = self.app.post('/students.json')
        data = json.loads(rv.data)
        assert data['last_name'] == 'Stanciu'
        assert data['first_name'] == 'Alex'
        
        
    def test_modify_student(self):
        
        rv = self.app.patch('/students/:id.json')
        data = json.loads(rv.data)
        assert data['first_name'] == 'Maries'
        assert data['last_name'] == 'Alexandru'

        
    def test_delete_student_id(self):
        
        rv = self.app.delete('/students/:id.json')
        data = json.loads(rv.data)
        assert data[0]['last_name'] == 'Muresan'
        assert data[0]['first_name'] == 'Ionut'
        assert data[1]['last_name'] == 'Minteuan'
        assert data[1]['first_name'] == 'Dan'
        
if __name__ == '__main__':
    unittest.main()