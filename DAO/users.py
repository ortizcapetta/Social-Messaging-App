

class userDAO:

    def __init__(self):
        self.users = [] # users in the "database"
        user0 = [111,'Alejandra','Ortiz',7875554444,'fakegamergirl@placeholder.com']
        user1 = [112,'Antonio','Lugo',9393332222,'tavern_brawler420@placeholder.com']
        user2 = [113,'Naruto','Uzumaki',1234567890,'ramenluvr@placeholder.com']
        user3 = [114,'Gustavo','Reyes',7871112222,'gustiiiiiii@placeholder.com']
        self.users.append(user0)
        self.users.append(user1)
        self.users.append(user2)
        self.users.append(user3)

    def getUsers(self):
        return self.users

    def getUsersID(self, uid): #searches for a specific ID in the DB
        result = []
        for a in self.users:
            if uid == a[0]:
                result.append(a)
        return result

    def getUsersEmail(self, email): #searches for email in the DB
        result = []
        for e in self.users:
            if email == e[4]:
                result.append(e)
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

