import os
from flask import Flask, render_template
from mongoengine import *

DEBUG = True
connect('tumblelog') # connect to mongodb

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/clasa.html')
def clasa(name = "Class Page"):
    return render_template('clasa.html')

@app.route('/clase.html')
def clase(name = "Clase Page"):
    return render_template('clase.html')

@app.route('/elev.html')
def elev(name = "Elev Page"):
    return render_template('elev.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
