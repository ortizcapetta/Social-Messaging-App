from DAO.users import *
from DAO.groups import *

class gUsersDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                  dbconfig['user'],
                                                  dbconfig['password'])

        self.connection = psycopg2._connect(curl)

    #NEED TO FIX

    #Get all groups of user with uid
    def getUserGroups(self, uid):
        cursor = self.connection.cursor()
        query = "select gid,gname,gowner from gUsers natural inner join groups where gUsers.uid = %s"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get all users in group with gid
    def getUsersInGroup(self, gid):
        cursor = self.connection.cursor()
        query = "select * from gUsers natural inner join Users where uID = %s;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
