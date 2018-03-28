from DAO.gUsers import *
from flask import *


class gUsersHandler:

    def buildgUserDict(self, row):
        gUsers = {}
        gUsers['gID'] = row[0]
        gUsers['uID'] = row[1]
        return gUsers

    #returns all users in specified group
    def getGroupUsers(self, gid):
        dao = gUsersDAO()
        users = dao.getUsersInGroup(gid)
        users_list = []
        for row in users:
            users_list.append(self.buildgUserDict(row))

        if users_list is None:
            return jsonify(Error="No users for this group in record")
        else:
            return jsonify(Users=users_list)

    #searches for groups specified user is in, might have to test what return value we want/need
    def getGroupsWithUser(self, uid):
        dao = gUsersDAO()
        groups = dao.getUserGroups(uid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildgUserDict(row))

        if groups_list is None:
            return jsonify(Error="No groups with this user in record")
        else:
            return jsonify(Groups=groups_list)