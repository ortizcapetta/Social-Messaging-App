from dbconfig import dbconfig
from sqlalchemy import text
import psycopg2

class repliesDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        #self.connection = psycopg2._connect(curl)

    #Get original message that the message is replying to
    def getOrigin(self, mid):
        #cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join messages on " \
                "replies.replyID = Messages.mID;"
        #cursor.execute(query,(mid,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get replies to given message
    def getReplies(self, mid):
        #cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join" \
                " Messages on Replies.replyID = Messages.mID where Replies.originID = %s;"
        #cursor.execute(query,(mid,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result
      
    def getAllReplies(self):
        #cursor = self.connection.cursor()
        query = "select mID as replyID,originID,uID,gID,timestamp,content from Replies inner join messages on " \
                "replies.replyID = Messages.mID;"
        #cursor.execute(query)
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result
