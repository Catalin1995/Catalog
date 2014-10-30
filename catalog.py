import os
from flask import Flask, render_template
from mongoengine import *

DEBUG = True
connect('tumblelog')
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(host='0.0.0.0', port=port)
    app.run()
