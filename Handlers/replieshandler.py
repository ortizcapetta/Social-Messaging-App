from DAO.replies import repliesDAO
from DAO.messages import *
from DAO.hashtags import *
from flask import *

class RepliesHandler:
    def buildRepliesDict(self, row):
        replies = {}
        replies['Message'] = row[0]
        replies['Reply'] = row[1]
        return replies

    def buildMessageDict(self, row):
        messages = {}
        messages['replyID'] = row[0]
        messages['originID'] = row[1]
        messages['uID'] = row[2]
        messages['gID'] = row[3]
        messages['timestamp'] = row[4]
        messages['content'] = row[5]
        messages['original'] = row[6]

        return messages

    #reply logging
    def addReply(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request") , 400
        else:
            originID = form.get("originID")
            #replyID = form.get("replyID")
            uid = form.get("uid")
            gid = form.get("gid")
            #timeStamp = form.get("timeStamp")
            content = form.get("content")
            if originID and uid and gid and content:
                dao = repliesDAO()
                mdao = messagesDAO()
                mid = mdao.addMessage(uid, gid, content)
                dao.addReply(originID, mid)
                htids = self.hashtagCheck(content, mid)
                return self.getRepliesByMessage(mid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def hashtagCheck(self, content, mid):
        if content.find("#") != -1:
            dao = hashtagsDAO()
            words = content.split(" ")
            htids = []
            for word in words:
                if(word[0] == "#"):
                    htids.append(dao.addHashtag(word, mid))
            return htids

    def getRepliesByMessage(self, mid):
        dao = repliesDAO()
        replies = dao.getReplies(mid)
        reply_list = []
        for row in replies:
            reply_list.append(self.buildMessageDict(row))
        return jsonify(Replies=reply_list)

    def getReplies(self):
        dao = repliesDAO()
        replies = dao.getAllReplies()
        reply_list = []
        for row in replies:
            reply_list.append(self.buildMessageDict(row))
        return jsonify(Replies=reply_list)

    def getRepliesbyDate(self, form):
        dao = repliesDAO()
        dateValue = form.get("timeStamp")
        name = dao.getAmountOfRepliesByDate(dateValue)
        reply_list = []
        for row in name:
            reply_list.append(self.buildMessageDict(row))
        return jsonify(Replies=reply_list)