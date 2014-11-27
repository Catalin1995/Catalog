import pep8
import unittest
import catalog
import tempfile
from flask import json
from email.quoprimime import body_check
from catalog.catalog import *
from tkinter.tix import NoteBook

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        Student.objects.delete()
        catalog.catalog.app.config['TESTING'] = True
        self.app = catalog.catalog.app.test_client()

    def create_student(self, first_name, last_name, clasa,
                       data_nasteri, adresa, alte_informati,
                       note, absente):
        student = dict(first_name=first_name,
                       last_name=last_name,
                       clasa=clasa,
                       data_nasteri=data_nasteri,
                       adresa=adresa,
                       alte_informati=alte_informati,
                       note = note,
                       absente = absente)
        rv = self.app.post('/students.json',
                           data=json.dumps(student),
                           content_type='application/json')
        data = json.loads(rv.data)
        return data

    def test_give_students(self):

        student = dict(first_name='Dan',
                       last_name='Ciprian',
                       clasa='9-D',
                       data_nasteri='5/5/1555',
                       adresa='Cluj',
                       alte_informati='Telefon: 5',
                       note = ['1','2','3','4'],
                       absente = ['10/10/2010', '20/20/2030'])
        rv = self.app.post('/students.json', data=json.dumps(student),
                           content_type='application/json')
        data = json.loads(rv.data)
        self.idStud = data['_id']['$oid']
        assert data['first_name'] == 'Dan'
        assert data['last_name'] == 'Ciprian'
        assert data['clasa'] == '9-D'
        assert data['data_nasteri'] == "5/5/1555"
        assert data['adresa'] == 'Cluj'
        assert data['alte_informati'] == 'Telefon: 5'
        assert data['note'] == ['1','2','3','4']
        assert data['absente'] == ['10/10/2010', '20/20/2030']

    def test_get_student_id(self):

        stud = self.create_student('Muresan', 'Ionut', '12-A',
                                   '27/10/1995', 'Dorobantilor 90',
                                   'Telefon: 10',
                                   ['10','10','10'],
                                   ['5/10/2013', '5/20/1010'])
        id = stud['_id']['$oid']
        rv = self.app.get('/students/'+id+'.json')
        data = json.loads(rv.data)
        assert data['first_name'] == "Muresan"
        assert data['last_name'] == 'Ionut'
        assert data['clasa'] == '12-A'
        assert data['data_nasteri'] == '27/10/1995'
        assert data['adresa'] == 'Dorobantilor 90'
        assert data['alte_informati'] == 'Telefon: 10'
        assert data['note'] == ['10','10','10']
        assert data['absente'] == ['5/10/2013', '5/20/1010']

    def test_modify_student(self):
 
        stud = self.create_student('Muresan', 'Ionut', '12-A',
                                   '27/10/1995', 'Dorobantilor 90',
                                   'Telefon: 10', ['10','10','10'],
                                   ['5/10/2013', '5/20/1010'])
        id = stud['_id']['$oid']
        student = dict(first_name='Zamisnicu',
                       last_name='Andreea',
                       clasa='10-D',
                       data_nasteri='01/03/1990',
                       adresa='Cluj',
                       alte_informati='Telefon: 3',
                       note = ['10','10','10'],
                       absente = ['5/10/2013', '5/20/1010'])
        rv = self.app.patch('/students/'+id+'.json',
                            data=json.dumps(student),
                            content_type='application/json')
        data = json.loads(rv.data)
 
        for i in range(len(data)):
            if data[i]['_id']['$oid'] == id:
                        assert data[i]['first_name'] == 'Zamisnicu'
                        assert data[i]['last_name'] == 'Andreea'
                        assert data[i]['clasa'] == '10-D'
                        assert data[i]['data_nasteri'] == '01/03/1990'
                        assert data[i]['adresa'] == 'Cluj'
                        assert data[i]['alte_informati'] == 'Telefon: 3'
                        assert data[i]['note'] == ['10','10','10']
                        assert data[i]['absente'] == ['5/10/2013', '5/20/1010']
                        break
 
    def test_delete_student_id(self):
  
        stud = self.create_student('Muresan', 'Ionut', '12-A',
                                   '27/10/1995', 'Dorobantilor 90',
                                   'Telefon: 10',
                                   ['10','10','10'],
                                   ['5/10/2013', '5/20/1010'])
        id = stud['_id']['$oid']
        rv = self.app.delete('/students/'+id+'.json')
        data = json.loads(rv.data)
        for i in range(len(data)):
            if data[i]['_id']['$oid'] == id:
                assert False
        assert True


if __name__ == '__main__':
    unittest.main()
