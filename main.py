from flask import Flask, request
from Handlers.userhandler import *
from Handlers.contactshandler import *
from Handlers.messageshandler import *


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Message App"

###########################
######Routes for Users######
###########################
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

@app.route('/users/contacts')
def getAllContacts():
    return ContactsHandler().getAllContacts()

@app.route('/users/email/<email>')  #by email
def getUserByEmail(email):
    return UserHandler().getUsersEmail(email)

@app.route('/users/phone/<int:phone>') #phone
def getUsersByPhone(phone):
    return UserHandler().getUsersPhone(phone)

@app.route('/users/name/<name>_<lname>') #full name, name and last name
def getUsersByFullName(name,lname):
    return UserHandler().getUsersFullName(name,lname)

@app.route('/users/name/<name>') #name can be either last name or first name, it will search for matches in both
def getUsersByName(name):
    return UserHandler().getUsersName(name)

#######################
##Routes for Messages##
#######################

@app.route('/users/messages')
def getAllMessages():
    return MessagesHandler().getMessages()

@app.route('/users/<int:uid>/messages')
def getMessagesByUser(uid):
    return MessagesHandler().getUserMessages(uid)

@app.route('/users/groups/<int:gid>/messages')
def getMessagesByGroup(gid):
    return MessagesHandler().getGroupMessages(gid)

@app.route('/users/messages/<int:mid>')
def getMessageByID(mid):
    return MessagesHandler().getMessageID(mid)
if __name__ == '__main__':
    app.run()