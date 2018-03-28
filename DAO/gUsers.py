from DAO.users import *
from DAO.groups import *

class gUsersDAO:
    def __init__(self):
        self.uInGroup = []
        user0 = [groupsDAO().groups[0][0], userDAO().users[0][0]]
        user1 = [groupsDAO().groups[1][0], userDAO().users[1][0]]
        user2 = [groupsDAO().groups[2][0], userDAO().users[2][0]]
        self.uInGroup.append(user0)
        self.uInGroup.append(user1)
        self.uInGroup.append(user2)

    #Get all groups of user with uid
    def getUserGroups(self, uid):
        result = []
        for a in self.uInGroup:
            if uid == a[1]:
                result.append(a[0])
        return result

    #Get all users in group with gid
    def getUsersInGroup(self, gid):
        result = []
        for a in self.uInGroup:
            if gid == a[0]:
                result.append(a[0])
        return result
