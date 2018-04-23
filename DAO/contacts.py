from dbconfig import dbconfig
import psycopg2

class contactsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    def getUserContacts(self, uid):
        cursor = self.connection.cursor()
        query = "select * from Contacts where uID= %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllContacts(self):
        cursor = self.connection.cursor()
        query = "select * from Contacts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result