from dbconfig import dbconfig
from sqlalchemy import text
import psycopg2

class hashtagsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        #self.connection = psycopg2._connect(curl)

    #Get all hashtags
    def getHashtags(self):
        #cursor = self.connection.cursor()
        query = "select * from hashtags;"
        #cursor.execute(query)
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    #Get hashtags by mID
    def getMessageHashtags(self, mid):
        #cursor = self.connection.cursor()
        query = "select * from Hashtags where mid = %s;"
        #cursor.execute(query,(mid,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by content
    def getContentHashtags(self, hashtag):
        #cursor = self.connection.cursor()
        query = "select * from Hashtags where hashtag = %s;"
        #cursor.execute(query,(hashtag,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by htID
    def getIdHashtags(self, htid):
        #cursor = self.connection.cursor()
        query = "select * from Hashtags where htid = %s;"
        #cursor.execute(query,(htid,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result