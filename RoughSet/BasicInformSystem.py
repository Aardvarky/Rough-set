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
        self._attributeNames = []
        self._attributeTypes = []
        self._objectNumber = 0

    def __del__(self):
        pass

    def setName(self, name):
        self._systemName = name

    def getName(self):
        return self._systemName

    def getSystemType(self):
        return self._systemType

    def setSystemType(self, type):
        self._systemType = type

    def getAttrNames(self):
        return self._attributeNames

    def setAttrNames(self, attrNames):
        self._attributeNames = attrNames

    def getAttrTypes(self):
        return self._attributeTypes

    def setAttrTypes(self, attrTypes):
        self._attributeTypes = attrTypes

    def getAttrName(self, index):
        if 0 <= index < len(self._attributeNames):
            return self._attributeNames[index]
        else:
            return ""

    def getAttrType(self, index):
        if 0 <= index < len(self._attributeTypes):
            return self._attributeTypes[index]
        else:
            return ""

    def getObjectNumber(self):
        return self._objectNumber

    def getObject(self, index):
        return self._objects.getObject(index)