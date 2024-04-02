from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/hello')
def hello():
    return '<h1>Hello flask</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {name}!</h1>'


@app.route('/user/<name>/<surname>')
def user_surname(name, surname):
    return '<h1>Hello, {name} {surname}!</h1>'


if __name__ == '__main__':
    app.run()
