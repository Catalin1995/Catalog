import os
import pep8
import catalog
import unittest
import tempfile
from flask import json
from catalog import Student
from email.quoprimime import body_check


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


    def test_get_student_id(self):
        
        rv = self.app.get('/students/0.json')
        data = json.loads(rv.data)
        assert data['first_name'] == 'Muresan'
        assert data['last_name'] == 'Ionut'
        assert data['clasa'] == '12-A'
        assert data['data_nasteri'] == '27/10/1995'
        assert data['adresa'] == 'Dorobantilor 90'
        assert data['alte_informati'] == 'Telefon: 1111111111'
        
        rv = self.app.get('/students/1000.json')
        data = json.loads(rv.data)
        assert data['Id'] == 'Id-ul este prea mare'
        
        rv = self.app.get('/students/-10.json')
        data = json.loads(rv.data)
        assert data['Id'] == 'Id-ul este prea mic'
        
        
    def test_get_students(self):
         
        rv = self.app.get('/students.json')
        data = json.loads(rv.data)
        assert data[0]['first_name'] == 'Muresan'
        assert data[0]['last_name'] == 'Ionut'
        assert data[0]['clasa'] == '12-A'
        assert data[0]['data_nasteri'] == '27/10/1995'
        assert data[0]['adresa'] == 'Dorobantilor 90'
        assert data[0]['alte_informati'] == 'Telefon: 1111111111'
        assert data[1]['first_name'] == 'Muresan'
        assert data[1]['last_name'] == 'Traian'
        assert data[1]['clasa'] == '11-B'
        assert data[1]['data_nasteri'] == '11/04/1995'
        assert data[1]['adresa'] == 'Dorobantilor 90'
        assert data[1]['alte_informati'] == 'Telefon: 2222222222'


    def test_give_students(self):
        # 
        student = dict(first_name='Dan', 
                   last_name='Ciprian',
                   clasa='9-D',
                   data_nasteri='5/5/1555',
                   adresa='Cluj',
                   alte_informati='Telefon: 5555555555')

        rv = self.app.post ('/students.json', data=json.dumps(student), content_type='application/json')
        data = json.loads(rv.data)
 
        assert data['first_name'] == 'Dan'
        assert data['last_name'] == 'Ciprian'
        assert data['clasa'] == '9-D'
        assert data['data_nasteri']     == "5/5/1555"
        assert data['adresa'] == 'Cluj'
        assert data['alte_informati'] == 'Telefon: 5555555555' 
            
    def test_modify_student(self):
        student = dict(first_name='Dan', 
                   last_name='Ciprian',
                   clasa='9-D',
                   data_nasteri='5/5/1555',
                   adresa='Cluj',
                   alte_informati='Telefon: 5555555555')

        rv = self.app.patch('/students/2.json', data=json.dumps(student), content_type='application/json')
        data = json.loads(rv.data)
        assert data['first_name'] == 'Dan'
        assert data['last_name'] == 'Ciprian'
        assert data['clasa'] == '9-D'
        assert data['data_nasteri'] == '5/5/1555'
        assert data['adresa'] == 'Cluj'
        assert data['alte_informati'] == 'Telefon: 5555555555'

    
    def test_delete_student_id(self):
          
        rv = self.app.delete('/students/2.json')
        data = json.loads(rv.data)
        assert data[0]['first_name'] == 'Muresan'
        assert data[0]['last_name'] == 'Ionut'
        assert data[0]['clasa'] == '12-A'
        assert data[0]['data_nasteri'] == '27/10/1995'
        assert data[0]['adresa'] == 'Dorobantilor 90'
        assert data[0]['alte_informati'] == 'Telefon: 1111111111'
        
if __name__ == '__main__':
    unittest.main()
