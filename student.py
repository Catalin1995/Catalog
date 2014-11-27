from mongoengine import Document, StringField, ListField


class Student(Document):
    
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    clasa = StringField(max_length=50)
    data_nasteri = StringField(max_length=50)
    adresa = StringField(max_length=50)
    alte_informati = StringField(max_length=50)
    note = ListField()
    absente = ListField()
    
    def update_student(self, new_stud):

        self.first_name = new_stud['first_name']
        self.last_name = new_stud['last_name']
        self.clasa = new_stud['clasa']
        self.data_nasteri = new_stud['data_nasteri']
        self.adresa = new_stud['adresa']
        self.alte_informati = new_stud['alte_informati']
        self.note = new_stud['note']
        self.absente = new_stud['absente']
