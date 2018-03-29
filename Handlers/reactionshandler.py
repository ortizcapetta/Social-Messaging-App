from DAO.reactions import *
from flask import *


class reactionsHandler:

    def buildgReactionsDict(self, row):
        reactions = {}
        reactions['uID'] = row[0]
        reactions['mID'] = row[1]
        reactions['LikeValue'] = row[2]
        return reactions

    #returns all reactions of message
    def getMessageReactions(self, mid):
        dao = reactionsDAO()
        reactions = dao.getReactions(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        if not reactions_list:
            return jsonify(Error="No reactions for that message in record"),404
        else:
            return jsonify(Reactions=reactions_list)

    #returns all liked/disliked messages of a user
    def getUserReactions(self, uid):
        dao = reactionsDAO()
        reactions = dao.getUserReactions(uid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        if not reactions_list:
            return jsonify(Error="No reactions for this user in record"),404
        else:
            return jsonify(Reactions=reactions_list)