import os
import unittest
import tempfile

from flask import json

import catalog
from catalog import Student


class StudentTestCase(unittest.TestCase):


    def setUp(self):

        catalog.app.config['TESTING'] = True
        self.app = catalog.app.test_client()


    def get_student(self):
        return Student(first_name="First", last_name= "Last")


    def test_get_students(self):
        student = self.get_student()
        student.save()

        for student in Student.objects:
            if student.first_name == "First":
                if student.last_name == "Last":
                    assert True
                else:
                    assert False
                

    def test_create_student(self):

        student = self.get_student()

        old_student_length = len(Student.objects)
        student.save()
        new_student_length = len(Student.objects)

        assert old_student_length, new_student_length - 1


    def test_update_student(self):

        student = self.get_student()

        student.first_name = "First_name"
        student.last_name = "Last_name"
        assert student.first_name != "First"
        assert student.last_name != "Last"


    def test_delete_student(self):

        student = self.get_student()
        student.save()
        old_student_length = len(Student.objects)
        student.delete()
        new_student_length = len(Student.objects)

        assert old_student_length == new_student_length + 1


if __name__ == '__main__':
    unittest.main()