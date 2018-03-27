from DAO.users import *
class chatGroupDAO:
    def __init__(self):
        self.groups = [] # users in the "database"
        group0 = [523,'Serious Anime Discussion Server',userDAO.getUsersID(111)]
        group1 = [231,'ICOM5016',userDAO.getUsersID(112)]
        group2 = [194,'Faaaaaaaam ;)', userDAO.getUsersID(114)]
        self.groups.append(group0)
        self.groups.append(group1)
        self.groups.append(group2)



