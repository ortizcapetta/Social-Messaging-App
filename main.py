from flask import Flask, request
from Handlers.userhandler import *
from Handlers.contactshandler import *
from Handlers.messageshandler import *
from Handlers.replieshandler import *
from Handlers.reactionshandler import *
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

@app.route('/users/<int:uid>/reactions') #search for user id's reactions
def getUserReactions(uid):
    return reactionsHandler().getUserReactions(uid)

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

##routes for replies##
@app.route('/users/messages/<int:mid>/replies')
def getRepliesByMessage(mid):
    return RepliesHandler().getRepliesByMessage(mid)

@app.route('/users/messages/replies')
def getAllReplies():
    return RepliesHandler().getReplies()

@app.route('/users/messages/<int:mid>/reactions') #search for message id's reactions
def getMessageReactions(mid):
    return reactionsHandler().getMessageReactions(mid)

###########################
######Routes for Groups######
###########################

@app.route('/users/groups') #get all groups
def getGroups():
    group = GroupsHandler()
    return group.getGroups()

@app.route('/users/groups/<int:gid>') #get all groups with ID
def getGroupsById(gid):
    group = GroupsHandler()
    return group.getGroupID(gid)

@app.route('/users/groups/<name>') #get all groups with Name
# need fixing
def getGroupsByName(gname):
    group = GroupsHandler()
    return group.getGroupName(gname)

@app.route('/users/<int:uid>/groups') #get all groups with User
def getUserGroups(uid):
    group = gUsersHandler()
    return group.getGroupsWithUser(uid)

@app.route('/users/<int:uid>/groups/owner') #get all groups owned by user
def getOwnerGroups(uid):
    group = GroupsHandler()
    return group.getGroupsOwnedBy(uid)

@app.route('/users/groups/<int:gid>/owner') #get group owner
def getGroupOwner(gid):
    group = GroupsHandler()
    return group.getGroupOwner(gid)


@app.route('/users/groups/<int:gid>/users') #get all users in group
def getGroupUsers(gid):
    users = gUsersHandler()
    return users.getGroupUsers(gid)


if __name__ == '__main__':
    app.run()
