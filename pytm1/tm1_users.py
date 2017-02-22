# coding=utf-8



import utils

common = utils.utils


class tm1_users(common):
    """
        Please insert comment here!
    """

    def __init__(self, tm1Base='http://localhost:8000/api/v1/', tm1AdminName='admin', tm1AdminPW='apple', debugLevel=0):
        """
            the default parameters for this class
        """

        # initialize Parent Class
        common.__init__(self, tm1Base, tm1AdminName, tm1AdminPW, debugLevel)

    def getListOf_Users(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Users")


    def getListOf_Groups(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Groups")


    # Users
    def addUserToGroup(self, tm1User, listOfGroups):
        """Please insert comment here!"""

        common.createOrUpdateODataRelationship(self, tm1User, "Users", "Groups", listOfGroups)


    def setPasswordForUser(self, tm1UserName, tm1UserPW):
        """Please insert comment here!"""

        taskname = "Set password for User - " + tm1UserName

        restCall = self.tm1Base + "Users"
        body = '{"Name": "' + tm1UserName + '", "Password": "' + tm1UserPW + '"}'

        common.tm1Post(self, restCall, body, taskname)


if __name__ == '__main__':

    print("This is not intended for direct use.")

