from dbconfig import dbconfig
import psycopg2

class hashtagsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    #Get all hashtags
    def getHashtags(self):
        cursor = self.connection.cursor()
        query = "select * from hashtags;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #used for logging new hashtags
    def addHashtag(self, hashtag, mid):
        cursor = self.connection.cursor()
        query = "insert into Hashtags(hashtag, mid) values ( %s, %s) returning htID"
        cursor.execute(query, (hashtag, mid,))
        htid = cursor.fetchone()[0]
        self.connection.commit()
        return htid

    def getMessagesWithHashtagsByGroup(self,gID):
        cursor = self.connection.cursor()
        query = "select htid,hashtags.mID, hashtag,content from hashtags natural inner join messages where gID = %s;"
        cursor.execute(query,(gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    
    #Get hashtags by gID
    def getGroupHashtags(self, gid):
        cursor = self.connection.cursor()
        query = "select htID, hashtag, mID from Hashtags inner join Messages where gid = %s;"
        cursor.execute(query,(gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by mID
    def getMessageHashtags(self, mid):
        cursor = self.connection.cursor()
        query = "select * from Hashtags where mid = %s;"
        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by content
    def getContentHashtags(self, hashtag):
        cursor = self.connection.cursor()
        query = "select * from Hashtags where hashtag = %s;"
        cursor.execute(query,(hashtag,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by content
    def getContentGroupHashtags(self, hashtag, gid):
        cursor = self.connection.cursor()
        query = "select htid,hashtags.mID, hashtag,content from Hashtags natural inner join Messages where hashtag = %s and gID = %s;"
        cursor.execute(query,(hashtag,gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by htID
    def getIdHashtags(self, htid):
        cursor = self.connection.cursor()
        query = "select * from Hashtags where htid = %s;"
        cursor.execute(query,(htid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get hashtags by popularity (top10)
    def getPopularHashtags(self):
        cursor = self.connection.cursor()
        query = "SELECT COUNT ( timeStamp::date ) AS Amount, hashtag, timeStamp::date " \
                "FROM Hashtags inner join Messages on hashtags.mid = messages.mid " \
                "GROUP BY hashtag, timeStamp::date " \
                "ORDER BY Amount DESC " \
                "LIMIT 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result