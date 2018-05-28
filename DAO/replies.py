from dbconfig import dbconfig
import psycopg2

class repliesDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    #Get original message that the message is replying to
    def getOrigin(self, mid):
        cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join messages on " \
                "replies.replyID = Messages.mID;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #used for logging new messages
    def addReply(self, originID, replyID):
        cursor = self.connection.cursor()
        query = "insert into Replies(originID, replyID) values ( %s, %s) returning mid"
        cursor.execute(query, (originID, replyID,))
        mid = cursor.fetchone()[0]
        self.connection.commit()
        return mid

    #Get replies to given message
    def getReplies(self, mid):
        cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join" \
                " Messages on Replies.replyID = Messages.mID where Replies.originID = %s;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
      
    def getAllReplies(self):
        cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join messages on " \
                "replies.replyID = Messages.mID;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
