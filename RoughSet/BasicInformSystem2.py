from BasicInformSystem import BasicInformSystem
from Bitset import Bitset
from CReductSet import CReductSet


class BasicInformSystem2(BasicInformSystem):
    """ Basic Information System 2"""

    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        super().__init__()

        self._reducts = CReductSet()
        self._core = Bitset(MAX_ATTRIBUTE_NUMBER)

        self._core.reset()

    def setObjectNumber(self, objectNumber):
        super().setObjectNumber(objectNumber)

    def setAttributeNumber(self, attributeNumber):
        super().setAttributeNumber(attributeNumber)

    def setAttributeIndexes(self, attributeIndexes):
        super().setAttributeIndexes(attributeIndexes)

    def compDependDegreeForAttribute(self, conAttr, decAttr):
        return super().compDependDegreeForAttribute(conAttr, decAttr)

    def compNondetRules(self, conAttr, decAttr):
        return super().compNondetRules(conAttr, decAttr)

    def getInformTable(self):
        return super().getInformTable()

    def getAttributeName(self, index):
        return super().getAttributeName(index)

    def compDiscernMatrix(self):
        super().compDiscernMatrix()

    def getAttributeNames(self):
        return super().getAttributeNames()

    def setName(self, name):
        super().setName(name)

    def getName(self):
        return super().getName()

    def getAttributeTypes(self):
        return super().getAttributeTypes()

    def getObjectName(self, index):
        return super().getObjectName(index)

    def getObject(self, index):
        return super().getObject(index)

    def getSystemType(self):
        return super().getSystemType()

    def getAttributeType(self, index):
        return super().getAttributeType(index)

    def compDependDegreeForAttributes(self, conAttr, decAttributes):
        return super().compDependDegreeForAttributes(conAttr, decAttributes)

    def setInformTable(self, informTable):
        super().setInformTable(informTable)

    def setAttributeNames(self, attributeNames):
        super().setAttributeNames(attributeNames)

    def getObjectNumber(self):
        return super().getObjectNumber()

    def getAttributeNumber(self):
        return super().getAttributeNumber()

    def setSystemType(self, systemType):
        super().setSystemType(systemType)

    def computeReducts(self):
        pass

    def computeReductsUsingAttributes(self):
        pass

    def saveReducts(self, file):
        pass

    def chooseAllReducts(self):
        for i in range(self.getReducts().size()):
            self.getReduct(i).setChoice(True)

    def chooseReducts(self, reductList):
        for i in range(len(reductList)):
            self.getReduct(reductList[i]).setChoice(True)

    def getReducts(self):
        return self._reducts

    def getReduct(self, index):
        return self._reducts.getReduct(index)