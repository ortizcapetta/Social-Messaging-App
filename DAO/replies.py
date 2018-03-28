from DAO.users import *
from DAO.messages import *

class repliesDAO:
    def __init__(self):
        self.reactions = []
        # [origin, reply]
        reply0 = [messagesDAO().messages[0][0], messagesDAO().messages[0][0]]
        reply1 = [messagesDAO().messages[0][0], messagesDAO().messages[1][0]]
        reply2 = [messagesDAO().messages[0][0], messagesDAO().messages[2][0]]
        self.reactions.append(reply0)
        self.reactions.append(reply1)
        self.reactions.append(reply2)

    #Get original message that the message is replying to
    def getOrigin(self, mid):
        result = []
        for a in self.reactions:
            if mid == a[0]:
                result.append(a[1])
        return result

    #Get replies to given message
    def getReplies(self, mid):
        result = []
        for a in self.reactions:
            if mid == a[1]:
                result.append(a[0])
        return result