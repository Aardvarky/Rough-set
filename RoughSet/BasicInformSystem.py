from Bitset import Bitset
from CDiscernMatrix import CDiscernMatrix
from CInformTable import CInformTable
from HashableDict import HashableDict
from CRuleSet import CRuleSet
from CRule import CRule


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

    def getAttributeNumber(self):
        return self._attributeNumber

    def setAttributeNumber(self, attributeNumber):
        self._attributeNumber = attributeNumber

    def getAttributeNames(self):
        return self._attributeNames

    def setAttributeNames(self, attributeNames):
        self._attributeNames = attributeNames

    def getAttributeName(self, index):
        if 0 <= index < len(self._attributeNames):
            return self._attributeNames[index]
        else:
            return ""

    def setAttributeIndexes(self, attributeIndexes):
        self._attributeIndexes = attributeIndexes

    def getAttributeType(self, index):
        if 0 <= index < len(self._attributeTypes):
            return self._attributeTypes[index]
        else:
            return ""

    def getAttributeTypes(self):
        return self._attributeTypes

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

    def compDiscernMatrix(self):
        self._objectNumber = self._objects.size()
        self._discernMatrix = CDiscernMatrix(self._objectNumber, self._attributeNumber)

        for i in range(self._objectNumber):
            for j in range(self._objectNumber):
                for k in range(self._attributeNumber):
                    x = self.getObject(i).getDescriptors().get(k)
                    y = self.getObject(j).getDescriptors().get(k)

                    if x != y:
                        self._discernMatrix.getImplicant(i, j).setValue(k)

    def compNondetRules(self, conAttr, decAttr):
        ruleSet = CRuleSet()
        tempRulesSet = CRuleSet()

        tempDiscMatrix = CDiscernMatrix(self._objectNumber, len(conAttr))
        for i in range(self._objectNumber):
            for j in range(self._objectNumber):
                for k in range(len(conAttr)):
                    x = self.getObject(i).getDescriptors().get(conAttr[k])
                    y = self.getObject(i).getDescriptors().get(conAttr[k])

                    if x == y:
                        tempDiscMatrix.getImplicant(i, j).setValue(conAttr[k])

        newDiscMatrix = CDiscernMatrix(self._objectNumber, len(conAttr))
        for i in range(self._objectNumber):
            for j in range(self._objectNumber):
                if i != j:
                    firstAttr = self.getObject(i).getDescriptors().get(decAttr)
                    secondAttr = self.getObject(j).getDescriptors().get(decAttr)

                    if firstAttr != secondAttr:
                        newDiscMatrix.getImplicant(i, j).assignOperator(tempDiscMatrix.getImplicant(i, j))

        for i in range(self._objectNumber):
            tempRulesSet.removeAll()
            numberOfRules = 0
            for j in range(self._objectNumber):
                if newDiscMatrix.getImplicant(i, j).any():
                    tempRulesSet.append(CRule())

                    for implicantIndex in range(newDiscMatrix.getImplicant(i, j).size()):
                        if newDiscMatrix.getImplicant(i, j).test(implicantIndex):
                            valueOfAttribute = self._objects.getObject(i).getDescriptors().get(implicantIndex)
                            tempRulesSet.getRule(numberOfRules).getAntecedent().add(implicantIndex, valueOfAttribute)

                    value = self._objects.getObject(i).getDescriptors().get(decAttr)
                    tempRulesSet.getRule(numberOfRules).getConsequent().add(decAttr, value)
                    numberOfRules += 1

            tempRulesSet.removeRules(0x00)
            for i in range(len(tempRulesSet.getRuleArray())):
                ruleSet.append(tempRulesSet.getRule(i))

        return ruleSet

    def compDependDegreeForAttribute(self, conAttr, decAttr):
        checkList = []
        totalCount = 0

        for i in range(self._objectNumber):
            checkList.append(False)

        for i in range(self._objectNumber - 1):
            if not checkList[i]:
                count = 1
                mark = False
                for j in range(i+1, self._objectNumber):
                    if self.getObject(i).compareUsingAttributesList(self.getObject(j), conAttr):
                        checkList[j] = True

                        if self.getObject(i).compareUsingAttribute(self.getObject(j), decAttr):
                            count += 1
                        else:
                            mark = True

                if not mark:
                    totalCount += count

        if not checkList[self._objectNumber - 1]:
            totalCount += 1

        return float(totalCount)/float(self._objectNumber)

    def compDependDegreeForAttributes(self, conAttr, decAttributes):
        checkList = []
        totalCount = 0

        for i in range(self._objectNumber):
            checkList.append(False)

        for i in range(self._objectNumber - 1):
            if not checkList[i]:
                count = 1
                mark = False
                for j in range(i + 1, self._objectNumber):
                    if self.getObject(i).compareUsingAttributesList(self.getObject(j), conAttr):
                        checkList[j] = True

                        if self.getObject(i).compareUsingAttributesList(self.getObject(j), decAttributes):
                            count += 1
                        else:
                            mark = True

                if not mark:
                    totalCount += count

        if not checkList[self._objectNumber - 1]:
            totalCount += 1

        return float(totalCount) / float(self._objectNumber)