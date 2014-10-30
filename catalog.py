from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
