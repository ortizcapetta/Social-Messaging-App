from flask import Flask, request
from Handlers.userhandler import *


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"
@app.route('/Users')
def getUsers():
    user = UserHandler()
    return user.getUsers()
@app.route('/Users/<int:uid>')
def getUserById(uid):
    return UserHandler().getUsersID(uid)

if __name__ == '__main__':
    app.run()