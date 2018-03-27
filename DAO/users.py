

class userDAO:

    def __init__(self):
        self.users = []
        user0 = [111,'Alejandra','Ortiz',7875554444,'fakegamergirl@placeholder.com']
        user1 = [112,'Antonio','Lugo',9393332222,'tavern_brawler420@placeholder.com']
        self.users.append(user0)
        self.users.append(user1)

    def getUsers(self):
        return self.users


    def getUsersID(self,uid):
        result = []
        for a in self.users:
            if uid == a[0]:
                result.append(a)
        return result