import os
from flask import Flask, render_template
from mongoengine import *

DEBUG = True
connect('tumblelog') # connect to mongodb

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clasa.html')
def clasa(name = "Class Page"):
    return render_template('clasa.html')

@app.route('/clase.html')
def clase(name = "Clase Page"):
    return render_template('clase.html')

@app.route('/elev.html')
def elev(name = "Elev Page"):
    return render_template('elev.html')

@app.route('/students.json')
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def all(self):
        return [] 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
 
