from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hi there'


@app.route('/SayHello/<username>')
def say_hello(username):
    return 'Hello %s' % username


if __name__  == '__main__':
    app.run(port=8001)
