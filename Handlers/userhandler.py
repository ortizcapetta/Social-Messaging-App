from DAO.users import userDAO
from flask import *


class UserHandler:

    def buildUserDict(self, row):
        users = {}
        users['uID'] = row[0]
        users['uFirstName'] = row[1]
        users['uLastName'] = row[2]
        users['password'] = row[3]
        users['phone'] = row[4]
        users['email'] = row[5]
        return users

    #get all users
    def getUsers(self):
        dao = userDAO()
        users = dao.getUsers()
        user_list = []
        for row in users:
            user_list.append(self.buildUserDict(row))

        return jsonify(Users=user_list)

    #search by ID
    def getUsersID(self,uid):
        dao = userDAO()
        uid = dao.getUsersID(uid)
        user_list = []
        for row in uid:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)
        
    #search by email
    def getUsersEmail(self,email):
        dao = userDAO()
        email = dao.getUsersEmail(email)
        user_list = []
        for row in email:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)
    #search by phone
    def getUsersPhone(self,phone):
        dao = userDAO()
        phone = dao.getUsersPhone(phone)
        user_list = []
        for row in phone:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)
    #search by full name
    def getUsersFullName(self,name,lname):
        dao = userDAO()
        name = dao.getUsersFullName(name,lname)
        user_list = []
        for row in name:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)

    #search by lname or fname
    def getUsersName(self,name):
        dao = userDAO()
        name = dao.getUsersName(name)
        user_list = []
        for row in name:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)

