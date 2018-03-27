from flask import Flask, request
from Handlers.userhandler import *
from Handlers.contactshandler import *


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"
@app.route('/Users') #get all users
def getUsers():
    user = UserHandler()
    return user.getUsers()


@app.route('/Users/<int:uid>') #get users by id num
def getUserById(uid):
    return UserHandler().getUsersID(uid)

@app.route('/Users/<int:uid>/contacts')
def getUserContacts(uid):
    return ContactsHandler().getUserContacts(uid)

@app.route('/Users/email/<email>')
def getUserByEmail(email):
    return UserHandler().getUsersEmail(email)

if __name__ == '__main__':
    app.run()