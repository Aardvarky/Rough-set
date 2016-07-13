from Bitset import Bitset
from CDiscernMatrix import CDiscernMatrix
from CInformTable import CInformTable


class BasicInformSystem:
    _attributes = Bitset()
    _discernMatrix = CDiscernMatrix()
    _objects = CInformTable()

    def __init__(self):
        self._attributes.reset()
        self._discernMatrix = None

        self._systemName = ""
        self._systemType = ""
        self._attributeNumber = 0
        self._attributeNames = []
        self._attributeIndexes = dict
        self._attributeTypes = []
        self._attributeCosts = []
        self._attributeValues = dict
        self._objectNumber = 0

    def getName(self):
        return self._systemName

    def setName(self, name):
        self._systemName = name

    def getSystemType(self):
        return self._systemType

    def setSystemType(self, type):
        self._systemType = type

    def getAttributeNumber(self):
        return self._attributeNumber

    def setAttributeNumber(self, attributeNumber):
        self._attributeNumber = attributeNumber

    def getAttributeNames(self):
        return self._attributeNames

    def setAttributeNames(self, attributeNames):
        self._attributeNames = attributeNames

    def getAttributeTypes(self):
        return self._attributeTypes

    def setAttributeTypes(self, attributeTypes):
        self._attributeTypes = attributeTypes

    def getAttributeName(self, index):
        if 0 <= index < len(self._attributeNames):
            return self._attributeNames[index]
        else:
            return ""

    def setAttributeName(self, index, stringValue):
        if 0 <= index < len(self._attributeNames):
            if type(stringValue) == str:
                self._attributeNames[index] = stringValue
            else:
                raise ValueError(stringValue)
        else:
            raise IndexError(index)

    def getAttributeType(self, index):
        if 0 <= index < len(self._attributeTypes):
            return self._attributeTypes[index]
        else:
            return ""

    def setAttributeType(self, index, stringValue):
        if 0 <= index < len(self._attributeNames):
            if type(stringValue) == str:
                self._attributeTypes[index] = stringValue
            else:
                raise ValueError(stringValue)
        else:
            raise IndexError(index)

    def getObjectNumber(self):
        return self._objectNumber

    def getObject(self, index):
        """ Repair this method! """
        return self._objects.getObject(index)

    def getInInformationTable(self):
        return self._objects