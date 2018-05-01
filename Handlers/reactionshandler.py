from DAO.reactions import *
from flask import *


class reactionsHandler:

    def buildgReactionsDict(self, row):
        reactions = {}
        reactions['rID'] = row[0]
        reactions['uID'] = row[1]
        reactions['mID'] = row[2]
        reactions['LikeValue'] = row[3]
        return reactions

    def buildReactDict(self, row):
        reactions = {}
        reactions['rID'] = row[0]
        reactions['uID'] = row[1]
        reactions['mID'] = row[2]
        return reactions


    #returns all reactions of message
    def getMessageReactions(self, mid):
        dao = reactionsDAO()
        reactions = dao.getReactions(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        return jsonify(Reactions=reactions_list)

        # returns all reactions of message

    def getMessageLikes(self, mid):
        dao = reactionsDAO()
        reactions = dao.getMessageLikes(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildReactDict(row))

        return jsonify(Reactions=reactions_list)

    def getMessageDislikes(self, mid):
        dao = reactionsDAO()
        reactions = dao.getMessageDislikes(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildReactDict(row))

        return jsonify(Reactions=reactions_list)

    #returns all liked/disliked messages of a user
    def getUserReactions(self, uid):
        dao = reactionsDAO()
        reactions = dao.getUserReactions(uid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        return jsonify(Reactions=reactions_list)

