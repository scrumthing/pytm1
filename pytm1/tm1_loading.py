# coding=utf-8

import utils

common = utils.utils


class tm1_loading(common):
    """
        Please insert comment here!
    """

    def __init__(self, tm1Base='http://localhost:8000/api/v1/', tm1AdminName='admin', tm1AdminPW='apple', debugLevel=0):
        """
            the default parameters for this class
        """

        # initialize Parent Class
        common.__init__(self, tm1Base, tm1AdminName, tm1AdminPW, debugLevel)


    def getListOf_Processes(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Processes")


    def getListOf_Chores(self):
        """Please insert comment here!"""
        return common.createListOfObjects(self, "Chores")

    def createProcess(self, tm1ProcessName, tm1ProcessProlog=""):
        '''Creates a Process'''

        taskname = "CREATE Process - " + tm1ProcessName

        restCall = self.tm1Base + "Processes"
        body = '{"Name": "' + tm1ProcessName + '", "PrologProcedure": "' + tm1ProcessProlog + '"}'
        print(body)

        common.tm1Post(self, restCall, body, taskname)

    def deleteProcess(self, tm1ProcessName ):
        '''Deletes a Process'''

        taskname = "DELETE Process - " + tm1ProcessName

        restCall = self.tm1Base + "Processes('" + tm1ProcessName + "')"

        common.tm1Delete(self, restCall, taskname)

    def executeProcess(self, tm1ProcessName ):
        '''Executes a Process'''

        taskname = "EXECUTE Process - " + tm1ProcessName

        restCall = self.tm1Base + "Processes('" + tm1ProcessName + "')/tm1.Execute"

        body = '{"Parameters": \
                       [\
                    ]\
                }'

        common.tm1Post(self, restCall, body, taskname)



if __name__ == '__main__':

    print("ATTENTION - This is not intended for direct use.")

    tm1Base = 'https://txtm1.tablonautix.com/api/v1/'
    tm1AdminName = 'admin'
    tm1AdminPW = 'apple'
    debugLevel = 5

    # initialize script
    tm1 = tm1_basicstructureinformation(tm1Base, tm1AdminName, tm1AdminPW, debugLevel)

    print(tm1.getListOf_Processes())
    print(tm1.getListOf_Chores())
