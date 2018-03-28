from DAO.groups import *
from flask import *


class GroupsHandler:

    def buildGroupDict(self, row):
        groups = {}
        groups['gID'] = row[0]
        groups['gName'] = row[1]
        groups['gOwner'] = row[2]
        return groups

    #returns all groups
    def getGroups(self):
        dao = groupsDAO()
        groups = dao.getGroups()
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        if groups_list is None:
            return jsonify(Error="No groups in record")
        else:
            return jsonify(Groups=groups_list)

    #searches for owner of a specific group
    def getGroupOwner(self, gid):
        dao = groupsDAO()
        gOwner = dao.getGroupOwner(gid)
        if gOwner is None:
            return jsonify(Error="No groups with ID in record")
        else:
            return jsonify(GroupOwner = gOwner)

    #searches for groups owned by specific user
    def getGroupsOwnedBy(self, uid):
        dao = groupsDAO()
        groups = dao.getOwnerGroups(uid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        if groups_list is None:
            return jsonify(Error="No groups owned in record")
        else:
            return jsonify(Groups=groups_list)

    #searches for groups with specific gid
    def getGroupID(self, gid):
        dao = groupsDAO()
        groups = dao.getGroupID(gid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        if groups_list is None:
            return jsonify(Error="No group with that ID in record")
        else:
            return jsonify(Groups=groups_list)

    #searches for groups with specific names
    def getGroupName(self, gname):
        dao = groupsDAO()
        groups = dao.getGroupName(gname)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        if groups_list is None:
            return jsonify(Error="No group with that name in record")
        else:
            return jsonify(Groups=groups_list)