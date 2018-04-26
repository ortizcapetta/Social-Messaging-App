from dbconfig import dbconfig
import psycopg2
from datetime import datetime

class messagesDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    #returns all messages in the DB
    def getMessages(self):
        cursor = self.connection.cursor()
        query = "select * from Messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns message content with matching ids
    def getMessageID(self, mid):
        cursor = self.connection.cursor()
        query = "select * from Messages where mID = %s;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns message id's with matching contents (strings only for now)
    def getMessageContent(self, content):
        cursor = self.connection.cursor()
        query = "select * from Messages where content = %s;"
        cursor.execute(query,(content,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns all message id's from group with gid
    #might need to edit once schema is updated because we might have to remove gid from Messages, if so use a natural inner join
    def getGroupMessages(self, gid):
        cursor = self.connection.cursor()
        query = "select * from Messages where gid = %s;"
        cursor.execute(query,(gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns message with a time-stamp (work in progress, need to test time/date datatypes)
    def getMessageTime(self, timeStamp):
        cursor = self.connection.cursor()
        query = "select * from Messages where timeStamp = %s;"
        cursor.execute(query,(timeStamp,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns messages sent by a user id
    def getMessageSentBy(self, uid):
        cursor = self.connection.cursor()
        query = "select * from Messages where uID = %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
