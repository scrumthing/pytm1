# coding=utf-8

import utils

common = utils.utils


class tm1_basicstructureinformation(common):
    """
        Please insert comment here!
    """

    def __init__(self, tm1Base='http://localhost:8000/api/v1/', tm1AdminName='admin', tm1AdminPW='apple', debugLevel=0):
        """
            the default parameters for this class
        """

        # initialize Parent Class
        common.__init__(self, tm1Base, tm1AdminName, tm1AdminPW, debugLevel)

    def getListOf_Dimensions(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Dimensions")


    def getListOf_Cubes(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Cubes")

    def getListOf_Processes(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Processes")

    def getListOf_Chores(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Chores")

    def getListOf_Users(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Users")

    def getListOf_Groups(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Groups")


if __name__ == '__main__':

    print("ATTENTION - This is not intended for direct use.")

    tm1Base = 'https://txtm1.tablonautix.com/api/v1/'
    tm1AdminName = 'admin'
    tm1AdminPW = 'apple'
    debugLevel = 5

    # initialize script
    tm1 = tm1_basicstructureinformation(tm1Base, tm1AdminName, tm1AdminPW, debugLevel)
    print(tm1.getListOf_Dimensions())
    print(tm1.getListOf_Cubes())
    print(tm1.getListOf_Processes())
    print(tm1.getListOf_Chores())
    print(tm1.getListOf_Users())
    print(tm1.getListOf_Groups())