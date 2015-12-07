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


class common:
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
                print(result.text)
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
                print(result.text)

    def convertJsonToList(self, result, jsonKey='value'):
        '''Takes a JSON Response and Creates a List for a Specific Key'''
        list = []
        parent = json.loads(result.text)["rows"]
        for item in parent:
            object = item[jsonKey]
            if object[0] != '}':
                list.append(object)
        return list

    def prettyPrintJson(self, result):
        '''Please insert comment here!'''
        prettyResult = (json.dumps(json.loads(result.text), indent=4, sort_keys=True))
        return prettyResult

    # region basic http functions
    def tm1GET(self, restCall, taskname):
        '''
            General GET Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT GET-operation"
        payload = ""

        result = self.dbConnection.get(restCall)
        self.errorHandling(taskname, restCall, result, payload)


    def tm1Post(self, restCall, body, taskname):
        '''
            General POST Operation on TM1
        '''

        if taskname == "":
            taskname = "DEFAULT POST-operation"
        payload = json.dumps(json.loads(body))

        result = self.dbConnection.post(restCall, data=payload)
        self.errorHandling(taskname, restCall, result, payload)


    def tm1Delete(self, restCall):
        '''General DELETE Operation on TM1'''

        result = self.dbConnection.delete(restCall)
        self.checkHttpResult(restCall, result)
        return result

    # endregion
