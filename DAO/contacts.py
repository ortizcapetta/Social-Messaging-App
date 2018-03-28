from DAO.users import *

class contactsDAO:
    def __init__(self):
        self.contacts = []
        contact0 = [userDAO().users[0][0], userDAO().users[1][0]]
        contact1 = [userDAO().users[0][0], userDAO().users[2][0]]
        contact2 = [userDAO().users[1][0], userDAO().users[2][0]]
        self.contacts.append(contact0)
        self.contacts.append(contact1)
        self.contacts.append(contact2)

    def getUserContacts(self, uid):
        result = []
        for a in self.contacts:
            if uid == a[0]:
                result.append(a[1])
            elif uid == a[1]:
                result.append(a[0])
        return result