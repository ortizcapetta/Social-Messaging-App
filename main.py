from flask import Flask, request
from Handlers.userhandler import *
from Handlers.contactshandler import *


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/users') #get all users
def getUsers():
    user = UserHandler()
    return user.getUsers()


@app.route('/users/<int:uid>') #get users by id num
def getUserById(uid):
    return UserHandler().getUsersID(uid)


@app.route('/users/<int:uid>/contacts') #view user's contact list
def getUserContacts(uid):
    return ContactsHandler().getUserContacts(uid)


@app.route('/users/email/<email>')  #search by email, not sure if necesary??
def getUserByEmail(email):
    return UserHandler().getUsersEmail(email)


if __name__ == '__main__':
    app.run()