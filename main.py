from flask import Flask, request, jsonify, render_template, flash, url_for, redirect
from Handlers.userhandler import *
from Handlers.contactshandler import *
from Handlers.messageshandler import *
from Handlers.replieshandler import *
from Handlers.reactionshandler import *
from Handlers.groupshandler import *
from Handlers.gUsershandler import *
from Handlers.hashtagshandler import *
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)
#below is code for connecting to heroku server, might break so if stuff blows up comment it out for now [only for SQLalchemy]
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/test')
def test_page():
    query = "select * from Users;"
    sql = text(query)
    cursor = db.engine.execute(sql)

    result = []
    for row in cursor:
        result.append(row)
    return result

@app.route('/')
def home():
    return "Welcome to Message App"


###########################
######Route for Login######
###########################

#untested, hard coded username/password for now as placeholder
@app.route('/login/', methods=["GET","POST"])
def login_page():

    error = ''
    try:
	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('getAllMessages'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)
    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)


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


##routes for reactions##
@app.route('/users/messages/<int:mid>/reactions') #search for message id's reactions
def getMessageReactions(mid):
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
@app.route('/users/messages/hashtags')
def getHashtags():
    return hashtagsHandler().getHashtags()



##########################
#####Routes for Groups####
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
