from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Sup.'


@app.route("/hi/")
def who():
    return "Who are you?"


@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"
