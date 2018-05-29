from DAO.messages import *
from flask import *


class MessagesHandler:
    def buildMessageDict(self,row):
        messages = {}
        messages['mID']= row[0]
        messages['uID'] = row[1]
        messages['gID'] = row[2]
        messages['timestamp'] = row[3]
        messages['content'] = row[4]
        return messages

    def buildMessageDict2(self,row):
        messages = {}
        messages['mID']= row[0]
        messages['uID'] = row[1]
        messages['gID'] = row[2]
        messages['timestamp'] = row[3]
        messages['content'] = row[4]
        messages['name'] = row[5] + " " + row[6] #ufirstname + ulastname
        messages['likes'] = row[7]
        messages['dislikes'] = row[8]
        return messages

    #message logging
    def addMessage(self, form):
            uid = form.get("uid")
            gid = form.get("gid")
            #removed timestamp because we can just put now()
            #timeStamp = form.get("timeStamp")
            content = form.get("content")
            if uid and gid and content:
                dao = messagesDAO()
                uid = dao.addMessage(uid, gid, content)
                return self.getMessageID(uid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getMessages(self):
        dao = messagesDAO()
        messages = dao.getMessages()
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict2(row))
        return jsonify(Messages=message_list)

    def getUserMessages(self,uid):
        dao = messagesDAO()
        messages = dao.getMessageSentBy(uid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict(row))

        return jsonify(Messages=message_list)


    def getGroupMessages(self,gid):
        dao = messagesDAO()
        messages = dao.getGroupMessages(gid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict2(row))

        return jsonify(Messages=message_list)

    def getMessageID(self,mid):
        dao = messagesDAO()
        messages = dao.getMessageID(mid)
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict2(row))

        return jsonify(Messages=message_list)
            