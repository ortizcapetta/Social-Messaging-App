from DAO.users import *
from DAO.groups import *
from datetime import datetime

class messagesDAO:
    def __init__(self):
        self.messages = []
        #check the date/time format, may be incorrect
        message0 = [111, userDAO().users[0][0], groupsDAO().groups[0][0], datetime.deltatime(), 'example content1']
        message1 = [222, userDAO().users[1][0], groupsDAO().groups[1][0], datetime.deltatime(), 'example content2']
        message2 = [333, userDAO().users[2][0], groupsDAO().groups[2][0], datetime.deltatime(), 'example content3']
        self.messages.append(message0)
        self.messages.append(message1)
        self.messages.append(message2)

    #returns message content with matching ids
    def getMessageID(self, mid):
        result = []
        for a in self.messages:
            if mid == a[0]:
                result.append(a[4])
        return result

    #returns message id's with matching contents (strings only for now)
    def getMessageContent(self, content):
        result = []
        for a in self.messages:
            if content == a[4]:
                result.append(a[0])
        return result

    #returns all message id's from group
    def getGroupMessages(self, gid):
        result = []
        for a in self.messages:
            if gid == a[2]:
                result.append(a[0])
        return result

    #returns message time-stamp given ids (work in progress, need to test time/date datatypes)
    def getMessageTime(self, mid):
        result = []
        for a in self.messages:
            if mid == a[0]:
                result.append(a[3])
        return result

    #returns messages sent by a user id
    def getMessageSentBy(self, uid):
        result = []
        for a in self.messages:
            if uid == a[1]:
                result.append(a[0])
        return result