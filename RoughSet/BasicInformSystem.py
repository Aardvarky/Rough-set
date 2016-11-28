from Bitset import Bitset
from CDiscernMatrix import CDiscernMatrix
from CInformTable import CInformTable
from HashableDict import HashableDict


class BasicInformSystem:
    def __init__(self):
        self._systemName = ""
        self._systemType = ""
        self._attributes = Bitset()
        self._attributeNumber = 0
        self._attributeNames = []
        self._attributeIndexes = HashableDict
        self._attributeTypes = []
        self._attributeCosts = []
        self._attributeValues = HashableDict

        self._objects = CInformTable()
        self._objectNumber = 0

        self._discernMatrix = CDiscernMatrix()

        self._attributes.reset()
        self._discernMatrix = None

    def getName(self):
        return self._systemName

    def setName(self, name):
        self._systemName = name

    def getSystemType(self):
        return self._systemType

    def setSystemType(self, systemType):
        self._systemType = systemType

    def getAttributeNames(self):
        return self._attributeNames

    def setAttributeNames(self, attributeNames):
        self._attributeNames = attributeNames

    def getAttributeName(self, index):
        if 0 <= index < len(self._attributeNames):
            return self._attributeNames[index]
        else:
            return ""

    def getAttributeType(self, index):
        if 0 <= index < len(self._attributeTypes):
            return self._attributeTypes[index]
        else:
            return ""

    def getObjectNumber(self):
        return self._objectNumber

    def setObjectNumber(self, objectNumber):
        self._objectNumber = objectNumber

    def getObject(self, index):
        if type(index) == int:
            return self._objects.getObject(index)
        else:
            raise TypeError(index)

    def getObjectName(self, index):
        if index < self._objectNumber:
            return self._objects.getObject(index).getName()
        else:
            return ""

    def getInformTable(self):
        return self._objects

    def setInformTable(self, informTable):
        self._objects.copyInstance(informTable)
