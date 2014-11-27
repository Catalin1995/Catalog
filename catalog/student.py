'''
Created on Nov 27, 2014

@author: ionut.muresan
'''
from mongoengine.fields import StringField, ListField
from mongoengine.document import Document

class Student(Document):

    first_name = StringField(max_length=50)     #reprezinta numele elevului
    last_name = StringField(max_length=50)      #reprezinta prenumele elevului
    clasa = StringField(max_length=50)          #reprezinta clasa in care se afla elevul
    data_nasteri = StringField(max_length=50)   #reprezinta data nasteri
    adresa = StringField(max_length=50)         #reprezinta adresa elevului
    alte_informati = StringField(max_length=50) #reprezinta alte informati despre elev
    note = ListField()                          #reprezinta o lista cu stringuri de note
    absente = ListField()                       #reprezinta o lista cu stringuri de absente
    
    def update_student(self, new_stud):

        self.first_name = new_stud['first_name']
        self.last_name = new_stud['last_name']
        self.clasa = new_stud['clasa']
        self.data_nasteri = new_stud['data_nasteri']
        self.adresa = new_stud['adresa']
        self.alte_informati = new_stud['alte_informati']
        self.note = new_stud['note']
        self.absente = new_stud['absente']