# coding=utf-8

import utils

common = utils.utils


class tm1_structure(common):
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


    def createDimension(self, tm1DimensionName):
        '''Creates a Dimension'''

        taskname = "CREATE Dimension - " + tm1DimensionName

        restCall = self.tm1Base + "Dimensions"
        body = '{"Name": "' + tm1DimensionName + '"}'

        common.tm1Post(self, restCall, body, taskname)


    def createDimensionElement(self, tm1DimensionName, tm1ElementName, tm1DimensionHierarchy=""):
        '''Adds an Element in a specific Dimension'''

        if tm1DimensionHierarchy == "":
            tm1DimensionHierarchy = tm1DimensionName

        taskname = "CREATE Element - " + tm1ElementName + " for Dimension - " + tm1DimensionName + " / Hierarchy - " + tm1DimensionHierarchy

        restCall = self.tm1Base + "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements"
        body = '{"Name": "' + tm1ElementName + '"}'

        common.tm1Post(self, restCall, body, taskname)


    def createDimensionAttribute(self, tm1DimensionName, tm1AttributName, tm1AttributType="String", tm1DimensionHierarchy=""):
        '''Adds an Element in a specific Dimension'''

        if tm1DimensionHierarchy == "":
            tm1DimensionHierarchy = tm1DimensionName

        taskname = "CREATE Attribute - " + tm1AttributName + "of Type - " + tm1AttributType + " for Dimension - " + tm1DimensionName + " / Hierarchy - " + tm1DimensionHierarchy

        restCall = self.tm1Base + "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/ElementAttributes"
        body = ' {"Name": "' + tm1AttributName + '", "Type": "' + tm1AttributType + '"}'

        common.tm1Post(self, restCall, body, taskname)


    def setElementParent(self, tm1DimensionName, tm1ElementName, tm1ElementParent, tm1DimensionHierarchy=""):
        '''Adds an Element in a specific Dimension'''

        if tm1DimensionHierarchy == "":
            tm1DimensionHierarchy = tm1DimensionName

        urlElementParent = "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements('" + tm1ElementParent + "')"
        urlElementName = "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements('" + tm1ElementName + "')"

        taskname = "SET Element - " + tm1ElementParent + " as Parent for Element - " + tm1ElementName

        restCall = self.tm1Base + "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Edges"
        body = '{"ParentName": "' + tm1ElementParent \
               + '", "ComponentName": "' + tm1ElementName \
               + '", "Parent@odata.bind": "' + urlElementParent \
               + '",  "Component@odata.bind": "' + urlElementName \
               + '",  "Weight": 1.0}'

        common.tm1Post(self, restCall, body, taskname)


    def setElementAttribute(self, tm1DimensionName, tm1ElementName, tm1AttributName, tm1AttributValue, tm1DimensionHierarchy=""):
        '''Untested because IBM has problems with PATCH and DELETE on this ressource'''

        if tm1DimensionHierarchy == "":
            tm1DimensionHierarchy = tm1DimensionName

        urlElementParent = "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements('" + tm1ElementParent + "')"
        urlElementName = "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements('" + tm1ElementName + "')"

        taskname = "SET Element - " + tm1ElementParent + " as Parent for Element - " + tm1ElementName

        restCall = self.tm1Base + "Dimensions('" + tm1DimensionName + "')/Hierarchies('" + tm1DimensionHierarchy + "')/Elements('" + tm1ElementName + "')/LocalizedAttributes"
        body = '{ "LocaleID": "Default", "Attributes": { "' \
               + tm1AttributName + '": "' \
               + tm1AttributValue + '"}}'

        common.tm1Post(self, restCall, body, taskname)


    def createOrUpdateCube(self, tm1CubeName, tm1ListOfDimensionsForCube):
        '''Creates a Cube'''

        common.createOrUpdateODataRelationship(self, tm1CubeName, "Cubes", "Dimensions", tm1ListOfDimensionsForCube)


if __name__ == '__main__':

    print("ATTENTION - This is not intended for direct use.")


