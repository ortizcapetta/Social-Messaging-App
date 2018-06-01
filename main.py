from flask import Flask, request, jsonify, render_template, flash, url_for, redirect, session
from Handlers.userhandler import *
from Handlers.contactshandler import *
from Handlers.messageshandler import *
from Handlers.replieshandler import *
from Handlers.reactionshandler import *
from Handlers.groupshandler import *
from Handlers.gUsershandler import *
from Handlers.hashtagshandler import *
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    #return render_template('index.html')
    return "Welcome to Message App"

###########################
#Routes for login/register#
###########################

@app.route('/register', methods = ['POST'])
def addUser():
    return UserHandler().addUser(request.get_json())

@app.route('/login', methods = ['POST'])
def loginUser():
    return UserHandler().loginUser(request.get_json())

###########################
#####Routes for Adding#####
###########################


###########################
####Routes for Getting#####
###########################



###########################
#####Routes for Users######
###########################

@app.route('/users') #get all users
def getUsers():
    user = UserHandler()
    return user.getUsers()


@app.route('/users/<int:uid>') #get users by id num
def getUserById(uid):
    return UserHandler().getUsersID(uid)


@app.route('/users/<int:uid>/contacts',methods=['GET']) #view user's contact list
def getUserContacts(uid):
    if request.method == 'GET':
        return ContactsHandler().getUserContacts(uid)

@app.route('/users/contacts', methods=['POST'])
def getAllContacts():
    if request.method == 'POST':
        return ContactsHandler().addUserContact(request.get_json())
    else:
        return ContactsHandler().getAllContacts()

@app.route('/users/email', methods=['GET'])  #by email
def getUserByEmail():
    if request.method == 'GET':
        return UserHandler().getUsersEmail(request.args)
    else:
        return ContactsHandler().getAllContacts()

@app.route('/users/phone', methods=['GET']) #phone
def getUsersByPhone():
    if request.method == 'GET':
        return UserHandler().getUsersPhone(request.args)
    else:
        return ContactsHandler().getAllContacts()

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

@app.route('/users/messages', methods=['GET'])
def getAllMessages():
    if request.method == 'GET':
      return MessagesHandler().getMessages()

@app.route('/users/<int:uid>/messages')
def getMessagesByUser(uid):
    return MessagesHandler().getUserMessages(uid)

#need to check how to add messages as replies as well in the same route, on hold for now
@app.route('/users/groups/<int:gid>/messages', methods=['GET','POST'])
def getMessagesByGroup(gid):
    if request.method == 'POST':

        return MessagesHandler().addMessage(request.get_json())
    else:
        return MessagesHandler().getGroupMessages(gid)

#getting hashtags in a group, else returns all hashtags
@app.route('/users/groups/<int:gid>/messages/hashtags', methods=['GET'])
def getMessagesHashtagsByGroup(gid):
    if request.method == 'GET':
        return hashtagsHandler().getMessageWithHashtagByGroup(gid)
    else:
        return hashtagsHandler().getHashtags()

@app.route('/users/messages/<int:mid>')
def getMessageByID(mid):
    return MessagesHandler().getMessageID(mid)

##routes for replies##
@app.route('/users/messages/<int:mid>/replies', methods = ['GET','POST'])
def getRepliesByMessage(mid):
    if request.method == 'POST':
        return RepliesHandler().addReply(request.get_json())
    else:
        return RepliesHandler().getRepliesByMessage(mid)

@app.route('/users/messages/replies')
def getAllReplies():
    return RepliesHandler().getReplies()


##routes for reactions##
@app.route('/users/messages/<int:mid>/reactions', methods=['GET','POST']) #search for message id's reactions
def getMessageReactions(mid):
    if request.method == 'POST':
        return reactionsHandler().addReaction(request.get_json())
    else:
        return reactionsHandler().getMessageReactions(mid)


@app.route('/users/messages/<int:mid>/reactions/likedby') #search for message id's reactions
def getMessageLikes(mid):
    return reactionsHandler().getMessageLikes(mid)


@app.route('/users/messages/<int:mid>/reactions/dislikedby') #search for message id's reactions
def getMessageDislikes(mid):
    return reactionsHandler().getMessageDislikes(mid)


@app.route('/users/messages/<int:mid>/reactions/numlikes') #search for message id's reactions
def getMessageLikesCount(mid):
    return reactionsHandler().getMessageLikeCount(mid)


@app.route('/users/messages/<int:mid>/reactions/numdislikes') #search for message id's reactions
def getMessageDislikesCount(mid):
    return reactionsHandler().getMessageDislikeCount(mid)

###routes for hashtags##
@app.route('/users/messages/hashtags', methods = ['GET'])
def getHashtags():
    hashtags = hashtagsHandler()
    if request.method == 'GET':
        return hashtags.getContentHashtags(request.get_json())
    else:
        return hashtags.getHashtags()



##########################
#####Routes for Groups####
##########################

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

@app.route('/users/<int:uid>/groups', methods = ["GET", "POST"]) #get all groups with User
def getUserGroups(uid):
    group = gUsersHandler()
    groupAdd = GroupsHandler()
    if(request.method == 'POST'):
        return groupAdd.addGroup(request.get_json())
    else:
        return group.getGroupsWithUser(uid)

@app.route('/users/<int:uid>/groups/owner') #get all groups owned by user
def getOwnerGroups(uid):
    group = GroupsHandler()
    return group.getGroupsOwnedBy(uid)

@app.route('/users/groups/<int:gid>/owner') #get group owner
def getGroupOwner(gid):
    group = GroupsHandler()
    return group.getGroupOwner(gid)


@app.route('/users/groups/<int:gid>/users', methods = ['POST','GET']) #get all users in group
def getGroupUsers(gid):
    group = gUsersHandler()
    if request.method == 'POST':
        return group.addGroupUser(request.get_json())

    else:
        return group.getGroupUsers(gid)
    

@app.route('/users/groups/hashtags', methods = ['GET'])
def getHashtagsByGroupContent():
    hashtags = hashtagsHandler()
    if request.method == 'GET':
        return hashtags.getContentGroupHashtags(request.args)
    else:
        return hashtags.getHashtags()

##########################
#####Routes for Charts####
##########################

@app.route('/charts/hashtags', methods=['GET']) #Trending topics via #hashtags (top 10)
def getPopularHashtags():
    hashtags = hashtagsHandler()
    if(request.method == 'GET'):
        return hashtags.getHashtagsbyDate(request.get_json())
    else:
        return hashtags.getHashtagsbyDate(request.get_json())

@app.route('/charts/messages', methods=['GET']) #Number of message per day
def getMessageNum():
    messages = MessagesHandler()
    if(request.method == 'GET'):
        return messages.getMessagesbyDate(request.args)
    else:
        return messages.getMessagesbyDate(request.args);

@app.route('/charts/replies', methods=['GET']) #Number of replies per day
def getRepliesNum():
    replies = RepliesHandler()
    if(request.method == 'GET'):
        return replies.getRepliesbyDate(request.get_json())
    else:
        return replies.getRepliesbyDate(request.get_json())

@app.route('/charts/likes', methods=['GET']) #Number of likes per day
def getLikesNum():
    reactions = reactionsHandler()
    if(request.method == 'GET'):
        return reactions.getLikesbyDate(request.get_json())
    else:
        return reactions.getLikesbyDate(request.get_json())

@app.route('/charts/dislikes', methods=['GET']) #Number of dislikes per day
def getDislikesNum():
    reactions = reactionsHandler()
    if(request.method == 'GET'):
        return reactions.getDislikesbyDate(request.get_json())
    else:
        return reactions.getDislikesbyDate(request.get_json())

@app.route('/charts/Users', methods=['GET']) #Active users posting messages or replies per day (top 10)
def getUsersNum():
    users = UserHandler()
    if(request.method == 'GET'):
        return users.getActiveUsersbyDate(request.get_json())
    else:
        return users.getActiveUsersbyDate(request.get_json())



if __name__ == '__main__':
    app.run()
