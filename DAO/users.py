

class userDAO:

    def __init__(self):
        self.users = []
        user0 = [111,'Alejandra','Ortiz',7876673629,'fakegamergirl@placeholder.com']
        self.users.append(user0)

    def getUsers(self):
        return self.users