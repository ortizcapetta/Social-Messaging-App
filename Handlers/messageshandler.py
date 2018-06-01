from DAO.messages import *
from DAO.hashtags import *
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

    def buildMessageDashDict(self,row):
        messages = {}
        messages['Count'] = row[0]
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
                mid = dao.addMessage(uid, gid, content)
                #htids isn't used atm but I'm putting it here in case we need to use it later
                htids = self.hashtagCheck(content, mid)
                return self.getMessageID(mid)
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

    def getMessagesWithHashtag(self, form):
        dao = messagesDAO()
        messages = dao.getMessagesWithHashtag(form.get("htID"))
        message_list = []
        for row in messages:
            message_list.append(self.buildMessageDict2(row))
        return jsonify(Messages=message_list)

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

    def getMessagesbyDate(self, form):
        dao = messagesDAO()
        dateValue = form.get("timeStamp")
        print(dateValue)

        name = dao.getAmountOfMessagesByDate(dateValue)
        message_list = []
        for row in name:
            message_list.append(self.buildMessageDashDict(row))
        return jsonify(Messages=message_list)
