from DAO.replies import repliesDAO
from flask import *

class RepliesHandler:
    def buildRepliesDict(self, row):
        replies = {}
        replies['Message'] = row[0]
        replies['Reply'] = row[1]
        return replies

    def buildMessageDict(self, row):
        messages = {}
        messages['mID'] = row[0]
        messages['uID'] = row[1]
        messages['gID'] = row[2]
        messages['timestamp'] = row[3]
        messages['content'] = row[4]

        return messages

    def getRepliesByMessage(self,mid):
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
            reply_list.append(self.buildRepliesDict(row))
        if not reply_list:
            return jsonify(Error = 'No replies'),404
        else:
            return jsonify(Replies=reply_list)