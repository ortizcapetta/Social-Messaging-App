from DAO.users import userDAO
from flask import *


class UserHandler:

    def buildUserDict(self, row):
        users = {}
        users['uID'] = row[0]
        users['uFirstName'] = row[1]
        users['uLastName'] = row[2]
        users['uPhone'] = row[3]
        users['uEMail'] = row[4]
        return users

    def getUsers(self):
        dao = userDAO()
        users = dao.getUsers()
        user_list = []
        for row in users:
            user_list.append(self.buildUserDict(row))

        if user_list is None:
            return jsonify(Error="No groups in record")
        else:
            return jsonify(Users=user_list)

    def getUsersID(self,uid):
        dao = userDAO()
        uid = dao.getUsersID(uid)

        if uid is None:
            return jsonify(Error="No User with ID in record")
        else:
            return jsonify(Users=uid)

    def getUsersEmail(self,email):
        dao = userDAO()
        email = dao.getUsersEmail(email)
        user_list = []
        for row in email:
            user_list.append(self.buildUserDict(row))

        if email is None:
            return jsonify(Error="No user found with the email %s" % email)
        else:
            return jsonify(Users=user_list)

    def getUsersPhone(self,phone):
        dao = userDAO()
        phone = dao.getUsersPhone(phone)
        user_list = []
        for row in phone:
            user_list.append(self.buildUserDict(row))

        if user_list is None:
            return jsonify(Error="No phone is system")
        else:
            return jsonify(Users=user_list)

    def getUsersFullName(self,name,lname):
        dao = userDAO()
        name = dao.getUsersFullName(name,lname)
        user_list = []
        for row in name:
            user_list.append(self.buildUserDict(row))

        if user_list is None:
            return jsonify(Error="No such name in system")
        else:
            return jsonify(Users=user_list)

    def getUsersName(self,name):
        dao = userDAO()
        name = dao.getUsersName(name)
        user_list = []
        for row in name:
            user_list.append(self.buildUserDict(row))
        if user_list is None:
            return jsonify(Error="No such name in system")
        else:
            return jsonify(Users=user_list)


    '''def getUserContacts(self,uid):
        dao = userDAO()
        contacts = dao.getUserContacts(uid)

        if contacts == None:
            return jsonify(Error="User has no friends :(")
        else:
            return jsonify(Users=contacts)'''

