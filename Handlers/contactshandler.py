from DAO.contacts import *
from flask import *


class ContactsHandler:

    def buildContactsDict(self, row):
        contacts = {}
        contacts['userID'] = row[0]
        contacts['friendID'] = row[1]

        return contacts
    #get contacts of a user
    def getUserContacts(self,uid):
        dao = contactsDAO()
        contact = dao.getUserContacts(uid)
        user_list = []
        for row in contact:
            user_list.append(self.buildContactsDict(row))

        if not user_list:
            return jsonify(Error="No records found"),404
        else:
            return jsonify(Contacs=contact)
    #get all contacts in system
    def getAllContacts(self):
        dao = contactsDAO()
        contacts = dao.getAllContacts()
        user_list = []
        for row in contacts:
            user_list.append(self.buildContactsDict(row))

        if not user_list:
            return jsonify(Error="No records found"),404
        else:
            return jsonify(Contacts=user_list)