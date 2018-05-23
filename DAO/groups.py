from DAO.users import *

class groupsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                  dbconfig['user'],
                                                  dbconfig['password'])

        self.connection = psycopg2._connect(curl)

    def getGroups(self):
        cursor = self.connection.cursor()
        query = "select * from Groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #searches for groups with specific owner
    def getOwnerGroups(self, uid):
        cursor = self.connection.cursor()
        query = "select * from Groups where gowner = %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #searches for owner of specific group

    #I think this is redundant but i'll leave it for now
    def getGroupOwner(self, gid):
        cursor = self.connection.cursor()

        query = "select uID,ufirstname,ulastname from groups inner join users on gOwner = uID where gID = %s"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #searches for groups with specific gid
    def getGroupID(self, gid):
        cursor = self.connection.cursor()
        query = "select * from Groups where gid = %s ;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #searches for groups with specific names
    def getGroupName(self, gname):
        cursor = self.connection.cursor()
        query = "select * from Groups where gname = %s;" ##have to edit this query and route too!!
        #what if names have spaces, how is that put on the url?
        cursor.execute(query, (gname,))
        result = []
        for row in cursor:
            result.append(row)
        return result