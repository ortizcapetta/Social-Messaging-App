from DAO.contacts import *
from flask import *


class ContactsHandler:

    def buildContactsDict(self, row):
        contacts = {}
        contacts['uID'] = row[0]
        contacts['friend'] = row[1]
        return contacts

    #testing some stuff with this
    #what i was talking about building the dicts
    def buildUserDict(self, row):
        users = {}
        users['uID'] = row[0]
        users['uFirstName'] = row[1]
        users['uLastName'] = row[2]
        users['password'] = row[3]
        users['phone'] = row[4]
        users['email'] = row[5]
        return users

    #get contacts of a user
    def getUserContacts(self,uid):
        dao = contactsDAO()
        contact = dao.getUserContacts(uid)
        user_list = []
        for row in contact:
            user_list.append(self.buildUserDict(row))
        return jsonify(Contacts=user_list)

    '''    def getUserContacts(self,uid):
        dao = contactsDAO()
        contact = dao.getUserContacts(uid)
        user_list = []
        for row in contact:
            user_list.append(self.buildContactsDict(row))

        if not user_list:
            return jsonify(Error="No records found"),404
        else:
            return jsonify(Contacs=contact)'''

    #get all contacts in system
    def getAllContacts(self):
        dao = contactsDAO()
        contacts = dao.getAllContacts()
        user_list = []
        for row in contacts:
            user_list.append(self.buildContactsDict(row))
        return jsonify(Contacts=user_list)