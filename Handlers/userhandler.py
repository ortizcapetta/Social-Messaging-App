from DAO.users import userDAO
from flask import *
from passlib.apps import custom_app_context as pwd_context

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

    def buildUserDict2(self, row):
        users = {}
        users['uID'] = row[0]
        users['Name'] = row[1] +" "+ row[2]
        users['password'] = row[3]
        users['phone'] = row[4]
        users['email'] = row[5]
        return users

    #user login
    def loginUser(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed post request") , 400
        else:
            email = form.get("email")
            #since the db stores the passwords already hashed, you need to hash the plain text pass to compare it in db w/ dao
            password = pwd_context.encrypt(form.get("password"))
            if email and password:
                dao = userDAO()
                if dao.getUsersEmail(email) != []:
                    user = self.getUsersEmailLogin(email)
                    if dao.getUsersPass(password) == dao.getUsersEmail(password):
                        return user
                    else:
                        return jsonify(Error="Invalid email or password"), 400
                else:
                    return jsonify(Error="Invalid email or password"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #user registration
    def addUser(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request") , 400
        else:
            fname = form.get("uFirstName")
            lname = form.get("uLastName")
            password = pwd_context.encrypt(form.get("password"))
            phoneNum = form.get("phoneNum")
            email = form.get("email")
            if fname and lname and password and phoneNum and email:
                dao = userDAO()
                if dao.getUsersEmail(email) !=[] or dao.getUsersPhone(phoneNum) !=[]:
                    return jsonify(Error="User already exists"), 400
                else:
                    uid = dao.addUser(fname, lname, password, phoneNum, email)
                    return self.getUsersID(uid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

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
    def getUsersEmailLogin(self,email):
        dao = userDAO()
        email = dao.getUsersEmail(email)
        user_list = []
        for row in email:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)
    #search by phone
    def getUsersPhoneLogin(self,phone):
        dao = userDAO()
        phone = dao.getUsersPhone(phone)
        user_list = []
        for row in phone:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)

    #search by email
    def getUsersEmail(self,form):
        dao = userDAO()
        email = dao.getUsersEmail(form.get("email"))
        user_list = []
        for row in email:
            user_list.append(self.buildUserDict2(row))
        return jsonify(Users=user_list)
    #search by phone
    def getUsersPhone(self,form):
        dao = userDAO()
        phone = dao.getUsersPhone(form.get("phone"))
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

    def getActiveUsersbyDate(self, form):
        dao = userDAO()
        dateValue = form.get("timeStamp")
        #dateValue = form.get("uFirstName")
        name = dao.getActiveUsersbyDate(dateValue)
        user_list = []
        for row in name:
            user_list.append(self.buildUserDict(row))
        return jsonify(Users=user_list)

