# coding=utf-8

# make sure requests is installed, be ware that there could be problems with proxies
# todo - solution for proxy-systems

pythonPackage = 'requests'
import importlib

try:
    importlib.import_module(pythonPackage)
except ImportError:
    import pip

    print(pip.main(['install', pythonPackage]))
finally:
    globals()[pythonPackage] = importlib.import_module(pythonPackage)

# import of necessary modules
import requests
import json
import os

class utils:
    def __init__(self, tm1Base='http://localhost:8000/api/v1/', tm1AdminName='admin', tm1AdminPW='apple', debugLevel=0):
        """
            the default parameters for this class
        """
        self.tm1Base = tm1Base
        self.tm1AdminName = tm1AdminName
        self.tm1AdminPW = tm1AdminPW
        self.debugLevel = debugLevel

        # warnings because of ssl-certification problem of tm1
        if debugLevel <= 1:
            requests.packages.urllib3.disable_warnings()

        # request session
        self.dbConnection = requests.Session()
        self.dbConnection.auth = (tm1AdminName, tm1AdminPW)
        self.dbConnection.verify = False
        self.dbConnection.headers = {'content-type': 'application/json'}


    def errorHandling(self, taskname, restCall, result, payload=""):
        """
            just a little helper function
            different error message for different debug levels
        """

        if result.ok:
            if self.debugLevel >= 3:
                print("> " + taskname + " was succesful.")
            if self.debugLevel >= 5:
                print("The following url was used:")
                print(restCall)
                if payload != "":
                    print("The following body was be used:")
                    print(payload)
                print("The following result was returned:")
                print(self.prettyPrintJson(result))
        else:
            if self.debugLevel >= 1:
                print("> " + taskname + " was not succesful.")
                print("> The following url was used:")
                print(restCall)
            if self.debugLevel >= 3:
                if payload != "":
                    print("The following body was be used:")
                    print(payload)
                print("The following result was returned:")
                print(self.prettyPrintJson(result))

        return 1

    def convertJsonToList(self, result, jsonKey='Name'):
        """
            Takes a JSON Response and Creates a List for a Specific Key
        """

        listOfObjects = []
        parent = json.loads(result)["value"]
        for item in parent:
            object = item[jsonKey]
            if object[0] != '}':
                listOfObjects.append(object)
        return listOfObjects


    def prettyPrintJson(self, result):
        """Please insert comment here!"""

        prettyResult = (json.dumps(json.loads(result.text), indent=4, sort_keys=True))

        return prettyResult


    # region basic http functions

    def tm1Get(self, restCall, taskname=""):
        '''
            General GET Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT GET-operation"
        payload = ""

        result = self.dbConnection.get(restCall)
        self.errorHandling(taskname, restCall, result, payload)
        return result


    def tm1Post(self, restCall, body, taskname=""):
        '''
            General POST Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT POST-operation"

        payload = json.dumps(json.loads(body))

        result = self.dbConnection.post(restCall, data=payload)
        self.errorHandling(taskname, restCall, result, payload)


    def tm1Patch(self, restCall, body, taskname=""):
        '''
            General POST Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT PATCH-operation"

        payload = json.dumps(json.loads(body))

        result = self.dbConnection.patch(restCall, data=payload)
        self.errorHandling(taskname, restCall, result, payload)


    def tm1Delete(self, restCall, taskname=""):
        '''
            General POST Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT DELETE-operation"

        payload = ""

        # check, if ressource exists
        checkHttp = self.tm1Get(restCall)
        if checkHttp.ok:
            result = self.dbConnection.delete(restCall)
            self.errorHandling(taskname, restCall, result, payload)
        else:
            print("ERROR - Ressource on " + restCall + " was not found!")


    # endregion

    def createListOfObjects(self, tm1Object="Users('Admin')"):
        """
            Requests a specific objekt from tm1 server and sends the recieved json to the function convertjsontolist.
        """

        taskname = "GET List Of " + tm1Object

        restCall = self.tm1Base + tm1Object

        result = self.tm1Get(restCall, taskname)
        ListOfObjects = self.convertJsonToList(result.text)
        return ListOfObjects


    def createOrUpdateODataRelationship(self, mainObject, mainObjectType, entity, listOfObjects):
        '''Adds an User to multiple groups'''

        taskname = "Create new relationship for " + mainObjectType + " and " + entity

        tempList = ""
        for object in listOfObjects:
            temp = '"' + entity + '(' + "'" + object + "'" + ')", '
            tempList = tempList + temp
        tempList = tempList[:-2]

        restCall = self.tm1Base + mainObjectType + "('" + mainObject + "')"
        body = '{"Name": "' + mainObject + '", "' + entity + '@odata.bind": [' + tempList + ']}'

        # check, if object already exists
        result = self.tm1Get(restCall, "Check, if object already exists.")

        if result.ok:
            self.tm1Patch(restCall, body, taskname)
        else:
            restCall = self.tm1Base + mainObjectType
            self.tm1Post(restCall, body, taskname)


if __name__ == '__main__':

    print("ATTENTION - This is not intended for direct use.")

