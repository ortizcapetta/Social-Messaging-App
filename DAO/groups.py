from DAO.users import *

class groupsDAO:
    def __init__(self):
        self.groups = []
        group0 = [111, 'nerds', userDAO().users[0][0],]
        group1 = [222,'friends', userDAO().users[1][0]]
        group2 = [333,'grupo de databases', userDAO().users[2][0]]
        self.groups.append(group0)
        self.groups.append(group1)
        self.groups.append(group2)

    def getGroups(self):
        return self.groups

    #searches for groups with specific owner
    def getOwnerGroups(self, uid):
        result = []
        for a in self.groups:
            if uid == a[2]:
                result.append(a)
        return result

    #searches for owner of specific group
    def getGroupOwner(self, gid):
        result = []
        for a in self.groups:
            if gid == a[0]:
                result.append(a)
        return result

    #searches for groups with specific gid
    def getGroupID(self, gid):
        result = []
        for a in self.groups:
            if gid == a[0]:
                result.append(a)
        return result

    #searches for groups with specific names
    def getGroupName(self, gname):
        result = []
        for a in self.groups:
            if gname == a[1]:
                result.append(a)
        return result
    
        
        
