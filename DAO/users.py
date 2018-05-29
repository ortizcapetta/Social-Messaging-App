from dbconfig import dbconfig
import psycopg2

class userDAO:

    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])

        self.connection = psycopg2._connect(curl)

    #used for registering users
    def addUser(self, fname, lname, password, phoneNum, email):
        cursor = self.connection.cursor()
        query = "insert into Users(uFirstName, uLastName, password, phoneNum, email) values ( %s, %s, %s, %s, %s ) returning uid"
        cursor.execute(query, (fname,lname,password,phoneNum,email,))
        uid = cursor.fetchone()[0]
        self.connection.commit()
        return uid

    def getUsers(self):
        cursor = self.connection.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersID(self, uid): #searches for a specific ID in the DB
        cursor = self.connection.cursor()
        query = "select * from Users where uID= %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersEmail(self, email): #searches for email in the DB
        cursor = self.connection.cursor()
        query = "select * from Users where email= %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersPhone(self,phone): #searches for phone in DB
        cursor = self.connection.cursor()
        query = "select * from Users where phoneNum= %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersName(self,name): #searches by name
        cursor = self.connection.cursor()
        query = "select * from Users where ufirstname = %s or ulastname = %s;"
        cursor.execute(query, (name, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersFullName(self,name, lname):
        cursor = self.connection.cursor()
        query = "select * from Users where ufirstname =%s and ulastname = %s;"
        cursor.execute(query, (name, lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersPass(self, password):
        cursor = self.connection.cursor()
        query = "select * from Users where password= %s;"
        cursor.execute(query, (password,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getActiveUsersbyDate(self, dateValue):
        cursor = self.connection.cursor()
        query = "SELECT COUNT ( uID ) AS Amount, uFirstName, uLastName" \
                "FROM Users inner join Messages on users.uid = messages.uid" \
                "WHERE (SELECT date_trunc('day', timeStamp)) as dateValue = %s" \
                "GROUP BY uFirstName" \
                "ORDER BY Amount DESC" \
                "LIMIT 10;"
        cursor.execute(query, (dateValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result