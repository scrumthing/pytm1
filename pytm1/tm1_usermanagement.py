# coding=utf-8

import utils

common = utils.utils


class tm1_usermanagement(common):
    """
        Please insert comment here!
    """

    def __init__(self, tm1Base='http://localhost:8000/api/v1/', tm1AdminName='admin', tm1AdminPW='apple', debugLevel=0):
        """
            the default parameters for this class
        """

        # initialize Parent Class
        common.__init__(self, tm1Base, tm1AdminName, tm1AdminPW, debugLevel)

    # Users
    def createTm1User(self, tm1UserName, tm1UserPW=""):
        """
            Please insert comment here!
        """

        taskname = "CREATE User - " + tm1UserName

        restCall = self.tm1Base + "Users"
        body = '{"Name": "' + tm1UserName + '", "Password": "' + tm1UserPW + '"}'

        common.tm1Post(self, restCall, body, taskname)

    def deleteTm1User(self, tm1UserName):
        """
            Please insert comment here!
        """

        taskname = "DELETE User - " + tm1UserName

        restCall = self.tm1Base + "Users('" + tm1UserName + "')"

        common.tm1Delete(self, restCall, taskname)

    #TODO - does not work properly

    '''
    def assignUser2Group(self, tm1User, tm1Group):
        """
            Assigns an Element a New Parent
        """

        taskname = "ADD User - " + tm1User + " to Group " + tm1Group

        urlElement = "Users('" + tm1User + "')"

        urlElementParent = "Groups('" + tm1Group + "')"

        restCall = self.tm1Base + "Users('" + tm1User + "')/Groups"
        body = '{"Name": "' + tm1Group + '", "Group@odata.bind": "' + urlElementParent + '}'

        print(body)
        print(restCall)
        common.tm1Post(self, restCall, body, taskname)
    '''

    # Groups
    def createTm1Group(self, tm1GroupName):
        """Please insert comment here! """

        taskname = "CREATE User - " + tm1GroupName

        restCall = self.tm1Base + "Groups"
        body = '{"Name": "' + tm1GroupName + '"}'

        common.tm1Post(self, restCall, body, taskname)

    def deleteTm1Group(self, tm1GroupName):
        """
            Please insert comment here!
        """

        taskname = "DELETE User - " + tm1GroupName

        restCall = self.tm1Base + "Groups('" + tm1GroupName + "')"

        common.tm1Delete(self, restCall, taskname)


if __name__ == '__main__':
    print("This is not intended for direct use.")