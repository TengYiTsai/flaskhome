from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/hello')
def hello():
    return '<h1>Hello flask</h1>'
