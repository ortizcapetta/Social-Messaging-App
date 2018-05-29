from dbconfig import dbconfig
import psycopg2

class reactionsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)


    #used for registering users
    def addReaction(self, uid, mid, likeValue):
        cursor = self.connection.cursor()
        query = "insert into Reactions(uid, mid, likeValue, timeStamp) values (%s, %s, %s, now()) returning rid"
        cursor.execute(query, (uid, mid, likeValue,))
        rid = cursor.fetchone()[0]
        self.connection.commit()
        return rid

    #Get reactions by time
    def getTimeReactions(self, timeStamp):
        cursor = self.connection.cursor()
        query = "select * from Reactions where reactTime = %s;"
        cursor.execute(query,(timeStamp,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get all messages user has reacted to, 0 for dislike, 1 for like
    def getUserReactions(self, uid):
        cursor = self.connection.cursor()
        query = "select * from Reactions where uid = %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get specific message user has reacted to, 0 for dislike, 1 for like
    def getUserMessageReaction(self, uid, mid):
        cursor = self.connection.cursor()
        query = "select * from Reactions where uid = %s and mid = %s;"
        cursor.execute(query,(uid, mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get reactions to a message
    def getReactions(self, mid):
        cursor = self.connection.cursor()
        query = "select reactions.mid,likeValue,count(likeValue) as num from " \
                "reactions " \
                "where reactions.mid = %s group by(reactions.mid,likeValue);" \


        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get reactions to a message
    def getMessageLikes(self,mid):
        likeValue =1
        cursor = self.connection.cursor()
        query = "select ufirstname,ulastname,users.uID from " \
                "reactions inner join users on reactions.uid = users.uid " \
                "where reactions.mid = %s and likeValue = %s;"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageDislikes(self, mid,):
        likeValue = -1
        cursor = self.connection.cursor()
        query = "select ufirstname,ulastname,users.uID from " \
                "reactions inner join users on reactions.uid = users.uid " \
                "where reactions.mid = %s and likeValue = %s;"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberofLikes(self,mid):
        likeValue = 1
        cursor = self.connection.cursor()
        query = "select mid,count(likeValue) from Reactions where mid = %s and likeValue = %s" \
                " group by(mid)"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get reactions with rID
    def getReactionsId(self, rid):
        cursor = self.connection.cursor()
        query = "select reactions.mid,likeValue,count(likeValue) as num from " \
                "reactions " \
                "where reactions.rid = %s group by(reactions.mid,likeValue);"
        cursor.execute(query,(rid,))

        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberofDislikes(self,mid):
        likeValue = -1
        cursor = self.connection.cursor()
        query = "select mid,count(likeValue) from Reactions where mid = %s and likeValue = %s" \
                " group by(mid)"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberofLikesByDate(self, dateValue):
        likeValue = 1
        cursor = self.connection.cursor()
        query = "SELECT COUNT ( rID )" \
                "FROM Reactions" \
                "WHERE (SELECT date_trunc('day', timeStamp)) AS dateValue = %s AND likeValue = %s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberofDislikesByDate(self, dateValue):
        likeValue = -1
        cursor = self.connection.cursor()
        query = "SELECT COUNT ( rID )" \
                "FROM Reactions" \
                "WHERE (SELECT date_trunc('day', timeStamp)) AS dateValue = %s AND likeValue = %s;"
        cursor.execute(query, (dateValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result