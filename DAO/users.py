from dbconfig import dbconfig
import psycopg2
class userDAO:

    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])

        self.connection = psycopg2._connect(curl)

        '''self.users = [] # users in the "database"
        user0 = [111,'Alejandra','Ortiz',7875554444,'aaaaaaaaaa@placeholder.com', 'password placeholder1']
        user1 = [112,'Antonio','Lugo',9393332222,'bbbbbbbbbb@placeholder.com', 'password placeholder2']
        user2 = [113,'Naruto','Uzumaki',1234567890,'ccccccccccc@placeholder.com', 'password placeholder3']
        user3 = [114,'Gustavo','Reyes',7871112222,'ddddddddddd@placeholder.com', 'password placeholder4']
        self.users.append(user0)
        self.users.append(user1)
        self.users.append(user2)
        self.users.append(user3)'''

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
        query = "select * from Users where uID= %s"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersEmail(self, email): #searches for email in the DB
        result = []
        for e in self.users:
            if email == e[4]:
                result.append(e)
        return result

    def getUsersPhone(self,phone): #searches for phone in DB
        result = []
        for p in self.users:
            if phone == p[3]:
                result.append(p)
        return result

    def getUsersName(self,name): #searches by name
        result = []
        for n in self.users:
            if name == n[1] or name == n[2]:
                result.append(n)
        return result

    def getUsersFullName(self,name,lname):
        result = []
        for n in self.users:
            if n[1] == name and n[2] == lname:
                result.append(n)
        return result

'''
    def getUserContacts(self,uid):
        if uid == 111:
            c = []
            c.append(self.users[3][0])
            c.append(self.users[1][0])
            c.append(self.users[2][0])
            return c
        elif uid == 112:
            return self.users[0][0]
        elif uid == 113:
            c = []
            c.append(self.users[0][0])
            c.append(self.users[1])
            return c
        elif uid ==114:
            return self.users[0][0]'''

