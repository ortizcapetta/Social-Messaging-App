from DAO.reactions import *
from flask import *


class reactionsHandler:

    def buildgReactionsDict(self, row):
        reactions = {}
        reactions['mID'] = row[0]
        reactions['likeValue'] = row[1]
        reactions['likeCount'] = row[2]
        return reactions

    def buildLikesDict(self, row):
        reactions = {}
        reactions['Name'] = row[0] + " " + row[1]
        reactions['uID'] = row[2]

        return reactions

    def buildLikesCountDict(self, row):
        reactions = {}
        reactions['mID'] = row[0]
        reactions['count'] = row[1]

        return 
        
    def buildReactionsDashDict(self,row):
        messages = {}
        messages['Count'] = row[0]
        messages['Date'] = row[1]
        return messages

    def buildLikesDashDict(self,row):
        messages = {}
        messages['Count'] = row[0]
        messages['Date'] = row[1]
        return messages
        
    def buildDislikesDashDict(self,row):
        messages = {}
        messages['Count'] = row[0]
        messages['Date'] = row[1]
        return messages

    def addReaction(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request") , 400
        else:
            uid = form.get("uID")
            mid = form.get("mID")
            likeValue = form.get("likeValue")
            if uid and mid:
                dao = reactionsDAO()
                if dao.getUserMessageReaction(uid, mid) !=[]:
                    return jsonify(Error="Reaction from user already exists for message"), 400
                else:
                    rid = dao.addReaction(uid, mid, likeValue)
                    return self.getIdReaction(rid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #returns all reactions w/ rid
    def getIdReaction(self, rid):
        dao = reactionsDAO()
        reactions = dao.getReactionsId(rid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        return jsonify(Reactions=reactions_list)

    #returns all reactions w/ timeStamp
    def getTimeReaction(self, timeStamp):
        dao = reactionsDAO()
        reactions = dao.getTimeReactions(timeStamp)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        return jsonify(Reactions=reactions_list)

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
            reactions_list.append(self.buildLikesDict(row))

        return jsonify(Reactions=reactions_list)


    def getMessageDislikes(self, mid):
        dao = reactionsDAO()
        reactions = dao.getMessageDislikes(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildLikesDict(row))

        return jsonify(Reactions=reactions_list)

    def getMessageLikeCount(self, mid):
        dao = reactionsDAO()
        reactions = dao.getNumberofLikes(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildLikesCountDict(row))

        return jsonify(Reactions=reactions_list)

    def getMessageDislikeCount(self, mid):
        dao = reactionsDAO()
        reactions = dao.getNumberofDislikes(mid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildLikesCountDict(row))

        return jsonify(Reactions=reactions_list)

    #returns all liked/disliked messages of a user
    def getUserReactions(self, uid):
        dao = reactionsDAO()
        reactions = dao.getUserReactions(uid)
        reactions_list = []
        for row in reactions:
            reactions_list.append(self.buildgReactionsDict(row))

        return jsonify(Reactions=reactions_list)

    def getReactionsbyDate(self):
        dao = reactionsDAO()
        name = dao.getNumberofLikesByDate()
        reaction_list = []
        for row in name:
            reaction_list.append(self.buildReactionsDashDict(row))
        return jsonify(Reactions=reaction_list)

    def getLikesbyDate(self):
        dao = reactionsDAO()
        name = dao.getNumberofLikesByDate()
        reaction_list = []
        for row in name:
            reaction_list.append(self.buildLikesDashDict(row))
        return jsonify(Reactions=reaction_list)

    def getDislikesbyDate(self):
        dao = reactionsDAO()
        name = dao.getNumberofDislikesByDate()
        reaction_list = []
        for row in name:
            reaction_list.append(self.buildDislikesDashDict(row))
        return jsonify(Reactions=reaction_list)