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
        users['Name'] = row[1] + " " + row[2]
        users['password'] = row[3]
        users['phone'] = row[4]
        users['email'] = row[5]
        return users

    #contact registration
    def addUserContact(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed post request") , 400
        else:
            uid = form.get("uid")
            friend = form.get("friend")

            if uid and friend:
                dao = contactsDAO()
                clause = friend in dao.getUserContacts(uid)
                print(clause)
                if clause:
                    return jsonify(Error="Contact already exists"), 400
                else:
                    uid = dao.addUserContact(uid, friend)
                    return self.getUserContacts(uid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

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