from flask import Flask, request
from Handlers.userhandler import *
from Handlers.contactshandler import *
from Handlers.groupshandler import *
from Handlers.gUsershandler import *

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


###########################
######Routes for Groups######
###########################

@app.route('/groups') #get all groups
def getGroups():
    group = GroupsHandler()
    return group.getGroups()

@app.route('/groups/<int:gid>') #get all groups with ID
def getGroupsById(gid):
    group = GroupsHandler()
    return group.getGroupID(gid)

@app.route('/groups/<name>') #get all groups with Name
def getGroupsByName(gname):
    group = GroupsHandler()
    return group.getGroupName(gname)

@app.route('users/<int:uid>/groups') #get all groups with User
def getUserGroups(uid):
    group = gUsersHandler()
    return group.getGroupsWithUser(uid)

@app.route('users/<int:uid>/groups/owners') #get all groups owned by user
def getOwnerGroups(uid):
    group = GroupsHandler()
    return group.getGroupsOwnedBy(uid)

@app.route('/groups/<int:gid>/users') #get all users in group
def getGroupUsers(gid):
    users = gUsersHandler()
    return users.getGroupUsers(gid)


########## not implemented yet
@app.route('/groups/messages/<int:mid>') #get all messages in group
def getGroupMessages(gid):
    group = GroupsHandler()
    return group.getGroups()


###########################
######Routes for Messages/Reactions######
###########################


if __name__ == '__main__':
    app.run()