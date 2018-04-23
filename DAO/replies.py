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
        query = "select * from Replies where replyID = %s;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get replies to given message
    def getReplies(self, mid):
        cursor = self.connection.cursor()
        query = "select * from Replies where originID = %s;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
      
    def getAllReplies(self):
        cursor = self.connection.cursor()
        query = "select * from Replies;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result