from DAO.contacts import *
from flask import *


class ContactsHandler:

    def buildUserDict(self, row): #not necessary? have to check
        contacts = {}
        contacts['userID'] = row[0]
        contacts['friendID'] = row[1]

        return contacts

    def getUserContacts(self,uid):
        dao = contactsDAO()
        contact = dao.getUserContacts(uid)
        if uid is None:
            return jsonify(Error="No User with ID in record")
        else:
            return jsonify(Contacs=contact)

    def getAllContacts(self):
        dao = contactsDAO()
        contacts = dao.getAllContacts()
        user_list = []
        for row in contacts:
            user_list.append(self.buildUserDict(row))
        return jsonify(Contacts=user_list)