from flask import Flask, render_template, request

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/send', methods=['POST'])
def send():
    return request.form['username']

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
