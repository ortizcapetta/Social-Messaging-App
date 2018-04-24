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
        #THIS IS THE UGLIEST THING I HAVE EVER DONE, PLEASE MAKE BETTER
        query = "select Contacts.uID,ufirstname,ulastname,password,phonenum,email from Contacts" \
                " inner join Users on Users.uID = Contacts.uID  where contacts.friend = %s " \
                " UNION ALL select friend as uID,ufirstname,ulastname,password,phonenum,email from Contacts" \
                " inner join Users on Users.uID = contacts.friend where Contacts.uID = %s;"
        cursor.execute(query, (uid,uid))
        result = []
        for row in cursor:
            result.append(row)
            print(row)

        return result

    def getAllContacts(self):
        cursor = self.connection.cursor()
        query = "select * from Contacts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result
