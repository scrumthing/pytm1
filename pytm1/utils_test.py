import utils
import json
import unittest

utils = utils.utils


class OfflineTest(unittest.TestCase):
    sampleJsonString= '{"@odata.context": "$metadata#Users", "value": [{"Name": "Admin", "Type": "Admin", "IsActive": true}, {"Name": "Usr1", "Type": "User", "IsActive": false}]}'
    sampleJsonAsList1 = ['Admin', 'Usr1']
    sampleJsonAsList2 = ['Admin', 'User']

    def test_convertJsonToList1(self):
        '''convertJsonToList should create a list, if a proper json is given'''

        result = utils.convertJsonToList(self, self.sampleJsonString)
        self.assertEqual(self.sampleJsonAsList1, result)


    def test_convertJsonToList2(self):
        '''convertJsonToList should create a list, if a different jsonkey is given'''

        result = utils.convertJsonToList(self, self.sampleJsonString, "Type")
        self.assertEqual(self.sampleJsonAsList2, result)

"""
class OnlineTest(unittest.TestCase):
    sampleJsonString= '{"@odata.context": "$metadata#Users", "value": [{"Name": "Admin", "Type": "Admin", "IsActive": true}, {"Name": "Usr1", "Type": "User", "IsActive": false}]}'
    sampleJsonAsList1 = ['Admin', 'Usr1']
    sampleJsonAsList2 = ['Admin', 'User']

    def test_convertJsonToList1(self):
        '''convertJsonToList should create a list, if a proper json is given'''

        result = utils.convertJsonToList(self, self.sampleJsonString)
        self.assertEqual(self.sampleJsonAsList1, result)
"""

if __name__ == '__main__':
    unittest.main()
