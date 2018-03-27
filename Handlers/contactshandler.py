from DAO.contacts import *
from flask import *


class ContactsHandler:

    def buildUserDict(self, row):
        contacts = {}
        contacts['uID'] = row[0]
        contacts['fID'] = row[1]

        return contacts

    def getUserContacts(self,uid):
        dao = contactsDAO()
        contact = dao.getUserContacts(uid)

        if uid == None:
            return jsonify(Error="No User with ID in record")
        else:
            return jsonify(Contacs=contact)
