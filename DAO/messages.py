from dbconfig import dbconfig
import psycopg2
from datetime import datetime

class messagesDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    '''#returns all messages in the DB
    def getMessages(self):
        cursor = self.connection.cursor()
        query = "select * from Messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        '''

    #used for logging new messages
    def addMessage(self, uid, gid,content):
        cursor = self.connection.cursor()
        query = "insert into Messages(uid, gid, timeStamp, content) values ( %s, %s, now(), %s) returning mid"
        cursor.execute(query, (uid, gid,content,))
        mid = cursor.fetchone()[0]
        self.connection.commit()
        return mid

    def getMessages(self):
        cursor = self.connection.cursor()
        '''query = "select mid,uid,gid,timestamp,content,ufirstname,ulastname from" \
                " Messages natural inner join users order by(timestamp) DESC;"'''

        query = "select Messages.mid,Messages.uid,gid,timestamp,content,ufirstname,ulastname," \
                "sum(case likeValue when 1 then 1 else 0 end) as likes,sum(case likeValue when -1 then 1 else 0 end) as dislikes" \
                " from Messages natural inner join users left join Reactions on Reactions.mID = Messages.mID " \
                "group by(Messages.mid,messages.uid,gid,timestamp,content,ufirstname,ulastname) order by(timestamp) DESC;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesWithHashtag(self, htID):
        cursor = self.connection.cursor()
        query = "select mid, uid, gid, timeStamp, content from Messages inner join Hashtags where htID = %s;"
        cursor.execute(query,(htID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #returns message content with matching ids
    def getMessageID(self, mid):
        cursor = self.connection.cursor()
        query = "select Messages.mid,Messages.uid,gid,timestamp,content,ufirstname,ulastname," \
                "sum(case likeValue when 1 then 1 else 0 end) as likes,sum(case likeValue when -1 then 1 else 0 end) as dislikes" \
                " from Messages natural inner join users left join Reactions on Reactions.mID = Messages.mID " \
                "where Messages.mID = %s group by(Messages.mid,messages.uid,gid,timestamp,content,ufirstname,ulastname) order by(timestamp) DESC;"
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
        query = query = "select Messages.mid,Messages.uid,gid,Messages.timestamp,content,ufirstname,ulastname," \
                "sum(case likeValue when 1 then 1 else 0 end) as likes,sum(case likeValue when -1 then 1 else 0 end) as dislikes" \
                " from Messages natural inner join users left join Reactions on Reactions.mID = Messages.mID " \
                "where Messages.gID =%s group by(Messages.mid,messages.uid,gid,timestamp,content,ufirstname,ulastname) order by(timestamp) DESC;"
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


    def getAmountOfMessagesByDate(self, timeStamp):
        cursor = self.connection.cursor()
        print(timeStamp)

        query = "SELECT COUNT (mID ) " \
                "FROM Messages " \
                "WHERE timeStamp::date = %s;"
        cursor.execute(query, (timeStamp,))
        result = []

        for row in cursor:

            result.append(row)
        return result
