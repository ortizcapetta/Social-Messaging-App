from DAO.replies import repliesDAO
from flask import *

class RepliesHandler:
    def buildRepliesDict(self, row):
        replies = {}
        replies['Message'] = row[0]
        replies['Reply'] = row[1]
        return replies

    def getRepliesByMessage(self,mid):
        dao = repliesDAO()
        replies = dao.getReplies(mid)
        reply_list = []
        for row in replies:
            reply_list.append(self.buildRepliesDict(row))

        if not reply_list:
            return jsonify(Error = 'No replies to message'),404
        else:
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