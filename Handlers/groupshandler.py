from DAO.groups import *
from flask import *


class GroupsHandler:

    def buildGroupDict(self, row):
        groups = {}
        groups['gID'] = row[0]
        groups['gName'] = row[1]
        groups['gOwner'] = row[2]
        return groups

    def buildOwnerDict(self,row):
        groups = {}
        groups['gID'] = row[0]
        groups['gName'] = row[1]
        groups['gOwner'] = row[2]

    #returns all groups
    def getGroups(self):
        dao = groupsDAO()
        groups = dao.getGroups()
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)

    #searches for owner of a specific group
    def getGroupOwner(self, gid):
        dao = groupsDAO()
        groups = dao.getGroupOwner(gid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildOwnerDict(row))
        return jsonify(GroupOwner=groups_list)

    #searches for groups owned by specific user
    def getGroupsOwnedBy(self, uid):
        dao = groupsDAO()
        groups = dao.getOwnerGroups(uid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)

    #searches for groups with specific gid
    def getGroupID(self, gid):
        dao = groupsDAO()
        groups = dao.getGroupID(gid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)

    #searches for groups with specific names
    def getGroupName(self, gname):
        dao = groupsDAO()
        groups = dao.getGroupName(gname)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)