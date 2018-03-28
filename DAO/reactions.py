from DAO.users import *
from DAO.messages import *

class reactionsDAO:
    def __init__(self):
        self.reactions = []
        reaction0 = [userDAO().users[0][0], messagesDAO().messages[0][0], 0]
        reaction1 = [userDAO().users[1][0], messagesDAO().messages[1][0], 1]
        reaction2 = [userDAO().users[2][0], messagesDAO().messages[2][0], 1]
        self.reactions.append(reaction0)
        self.reactions.append(reaction1)
        self.reactions.append(reaction2)

    #Get all messages user has reacted to, 0 for dislike, 1 for like
    def getUserReactions(self, uid):
        result = []
        for a in self.reactions:
            if uid == a[0]:
                result.append(a)
        return result

    #Get reactions to a message
    def getReactions(self, mid):
        result = []
        for a in self.reactions:
            if mid == a[1]:
                result.append(a)
        return result
