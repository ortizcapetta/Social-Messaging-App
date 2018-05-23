from dbconfig import dbconfig
from sqlalchemy import text
import psycopg2

class userDAO:

    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])

        #self.connection = psycopg2._connect(curl)
        #commented out the method for local DB and added for heroku, might break


    def getUsers(self):
        #cursor = self.connection.cursor()
        query = "select * from Users;"
        #cursor.execute(query)
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)

        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersID(self, uid): #searches for a specific ID in the DB
        #cursor = self.connection.cursor()
        query = "select * from Users where uID= %s;"
        #cursor.execute(query,(uid,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersEmail(self, email): #searches for email in the DB
        #cursor = self.connection.cursor()
        query = "select * from Users where email= %s;"
        #cursor.execute(query, (email,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersPhone(self,phone): #searches for phone in DB
        #cursor = self.connection.cursor()
        query = "select * from Users where phone= %s;"
        #cursor.execute(query, (phone,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersName(self,name): #searches by name
        #cursor = self.connection.cursor()
        query = "select * from Users where ufirstname = %s or ulastname = %s;"
        #cursor.execute(query, (name, name,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersFullName(self,name, lname):
        #cursor = self.connection.cursor()
        query = "select * from Users where ufirstname =%s and ulastname = %s;"
        #cursor.execute(query, (name, lname,))
        from main import db
        sql = text(query)
        cursor = db.engine.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        return result

