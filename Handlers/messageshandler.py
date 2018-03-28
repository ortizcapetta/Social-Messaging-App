from DAO.messages import *
from flask import *


class MessagesHandler:
    def buildMessageDict(self,row):
        messages = {}
        messages['mID']= row[0]
        messages['sentBy'] = row[1]
        messages['gID'] = row[2]
        messages['timestamp'] = row[3]
        messages['content'] = row[4]
        return messages

    def getMessages(self):
        dao = messagesDAO()
        messages = dao.getMessages()
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict(row))
        return jsonify(Messages=message_list)

    def getUserMessages(self,uid):
        dao = messagesDAO()
        messages = dao.getMessageSentBy(uid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict(row))

        if message_list is None:
            return jsonify(Error="User has sent no messages")
        else:
            return jsonify(Messages=message_list)


    def getGroupMessages(self,gid):
        dao = messagesDAO()
        messages = dao.getGroupMessages(gid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict(row))

        if message_list is None:
            return jsonify(Error="No messages in group")
        else:
            return jsonify(Messages=message_list)

    def getMessageID(self,mid):
        dao = messagesDAO()
        messages = dao.getMessageID(mid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict(row))

        if message_list is None:
            return jsonify(Error="No messages with that id")
        else:
            return jsonify(Messages=message_list)
            