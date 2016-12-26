from BasicInformSystem import BasicInformSystem
from Bitset import Bitset
from CReductSet import CReductSet
from CImplArray import CImplArray
from CComputingRules import CComputingRules


class BasicInformSystem2(BasicInformSystem):

    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        super().__init__()

        self._reducts = CReductSet()
        self._core = Bitset(MAX_ATTRIBUTE_NUMBER)

        self._core.reset()

    def getObjectName(self, index):
        return super().getObjectName(index)

    def compDependDegreeForAttributes(self, conAttr, decAttributes):
        return super().compDependDegreeForAttributes(conAttr, decAttributes)

    def setAttributeValues(self, attributeValues):
        super().setAttributeValues(attributeValues)

    def getAttributeIndexes(self):
        return super().getAttributeIndexes()

    def setAttributeNames(self, attributeNames):
        super().setAttributeNames(attributeNames)

    def setSystemType(self, systemType):
        super().setSystemType(systemType)

    def setAttributeCosts(self, attributeCosts):
        super().setAttributeCosts(attributeCosts)

    def getObjects(self):
        return super().getObjects()

    def getDiscernMatrix(self):
        return super().getDiscernMatrix()

    def compDependDegreeForAttribute(self, conAttr, decAttr):
        return super().compDependDegreeForAttribute(conAttr, decAttr)

    def getAttributeCosts(self):
        return super().getAttributeCosts()

    def getAttributeName(self, index):
        return super().getAttributeName(index)

    def getAttributeNumber(self):
        return super().getAttributeNumber()

    def setAttributeIndexes(self, attributeIndexes):
        super().setAttributeIndexes(attributeIndexes)

    def setAttributes(self, bits=0):
        super().setAttributes(bits)

    def setObject(self, index, globalState):
        super().setObject(index, globalState)

    def compNondetRules(self, conAttr, decAttr):
        return super().compNondetRules(conAttr, decAttr)

    def getName(self):
        return super().getName()

    def getInformTable(self):
        return super().getInformTable()

    def setInformTable(self, informTable):
        super().setInformTable(informTable)

    def getAttributeNames(self):
        return super().getAttributeNames()

    def setAttributeTypes(self, attributeTypes):
        super().setAttributeTypes(attributeTypes)

    def setAttributeNumber(self, attributeNumber):
        super().setAttributeNumber(attributeNumber)

    def getAttributeValues(self):
        return super().getAttributeValues()

    def setObjectNumber(self, objectNumber):
        super().setObjectNumber(objectNumber)

    def getAttributeType(self, index):
        return super().getAttributeType(index)

    def getSystemType(self):
        return super().getSystemType()

    def setObjectName(self, index, name):
        super().setObjectName(index, name)

    def compDiscernMatrix(self):
        super().compDiscernMatrix()

    def getObject(self, index):
        return super().getObject(index)

    def setName(self, name):
        super().setName(name)

    def getAttributes(self):
        return super().getAttributes()

    def getObjectNumber(self):
        return super().getObjectNumber()

    def getAttributeTypes(self):
        return super().getAttributeTypes()

    def setObjects(self, objects):
        super().setObjects(objects)

    def computeReducts(self):
        firstCComputingRules = CComputingRules()
        implicents = CImplArray()
        implicants = CImplArray()

        self.compDiscernMatrix()

        i = 0
        j = 0
        while i < self._objectNumber:
            while j < i:
                if self.getDiscernMatrix().getImplicant(i, j).any():
                    implicents.append(self.getDiscernMatrix().getImplicant(i, j))

                if self.getDiscernMatrix().getImplicant(i, j).count(1) == 1:
                    self._core.orOperat(self.getDiscernMatrix().getImplicant(i, j))
                j += 1
            i += 1

        if implicents.size() != 0:
            implicants.assignOperator(firstCComputingRules.minimDiscFunc(implicents))

        self._reducts.write(implicants, self.getAttributeNumber())

    def computeReductsUsingAttributes(self, startIndex, stopIndex):
        self._reducts.removeAll()

        firstCComputingRules = CComputingRules()
        implicents = CImplArray()
        implicants = CImplArray()

        i = startIndex
        while i <= stopIndex:
            j = startIndex
            while j < i:
                if self.getDiscernMatrix().getImplicant(i, j).any():
                    implicents.append(self.getDiscernMatrix().getImplicant(i, j))

                if self.getDiscernMatrix().getImplicant(i, j).count(1) == 1:
                    self._core.orOperat(self.getDiscernMatrix().getImplicant(i, j))
                j += 1
            i += 1

        if implicents.size() != 0:
            implicants.assignOperator(firstCComputingRules.minimDiscFunc(implicents))

        self._reducts.write(implicants, self.getAttributeNumber())

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