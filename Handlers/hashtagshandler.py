from DAO.hashtags import *
from flask import *


class hashtagsHandler:

    def buildgHashtagsDict(self, row):
        hashtags = {}
        hashtags['htID'] = row[0]
        hashtags['mID'] = row[1]
        hashtags['hashtag'] = row[2]
        return hashtags
    def buildgHashtagsDict2(self, row):
        hashtags = {}
        hashtags['htID'] = row[0]
        hashtags['mID'] = row[1]
        hashtags['hashtag'] = row[2]
        hashtags['content'] = row[3]
        return hashtags


    #returns all hashtags of message
    def getMessageHashtags(self, mid):
        dao = hashtagsDAO()
        hashtags = dao.getMessageHashtags(mid)
        hashtags_list = []
        for row in hashtags:
            hashtags_list.append(self.buildgHashtagsDict(row))

        return jsonify(hashtags=hashtags_list)

    #returns all hashtags with content
    def getContentHashtags(self, content):
        dao = hashtagsDAO()
        hashtags = dao.getContentHashtags(content)
        hashtags_list = []
        for row in hashtags:
            hashtags_list.append(self.buildgHashtagsDict(row))

        return jsonify(hashtags=hashtags_list)

    def getMessageWithHashtagByGroup(self,gID):
        dao = hashtagsDAO()
        hashtags = dao.getMessagesWithHashtagsByGroup(gID)
        hashtags_list = []
        for row in hashtags:
            hashtags_list.append(self.buildgHashtagsDict2(row))

        return jsonify(hashtags=hashtags_list)

    #get all hashtags with id
    def getMessageDislikes(self, htid):
        dao = hashtagsDAO()
        hashtags = dao.getIdHashtags(htid)
        hashtags_list = []
        for row in hashtags:
            hashtags_list.append(self.buildgHashtagsDict(row))

        return jsonify(hashtags=hashtags_list)

    #get all hashtags
    def getHashtags(self):
        dao = hashtagsDAO()
        hashtags = dao.getHashtags()
        hashtags_list = []
        for row in hashtags:
            hashtags_list.append(self.buildgHashtagsDict(row))

        return jsonify(hashtags=hashtags_list)
