from DAO.gUsers import *
from flask import *


class gUsersHandler:

    def buildgUserDict(self, row):
      users = {}
      users['uID'] = row[0]
      users['uFirstName'] = row[1]
      users['uLastName'] = row[2]
      return users

    def buildGroupDict(self, row):
        groups = {}
        groups['gID'] = row[0]
        groups['gName'] = row[1]
        groups['gOwner'] = row[2]
        return groups

    #returns all users in specified group
    def getGroupUsers(self, gid):
        dao = gUsersDAO()
        users = dao.getUsersInGroup(gid)
        users_list = []
        for row in users:
            users_list.append(self.buildgUserDict(row))

        return jsonify(Users=users_list)

    #searches for groups specified user is in
    def getGroupsWithUser(self, uid):
        dao = gUsersDAO()
        groups = dao.getUserGroups(uid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)