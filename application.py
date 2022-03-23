from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Sup.'


@application.route("/hi/")
def who():
    return "Who are you?"


@application.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"
