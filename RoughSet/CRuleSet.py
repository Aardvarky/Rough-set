from CRule import CRule


class CRuleSet(list):
    def __init__(self):
        self.__ruleArray = []

    def copyInstance(self, RuleSet):
        if isinstance(RuleSet, self.__class__):
            for i in self.__ruleArray:
                del i

            for i in RuleSet.getRuleArray():
                self.__ruleArray.append(i)
        else:
            raise TypeError(RuleSet)

    def append(self, rule):
        if isinstance(rule, CRule):
            self.__ruleArray.append(rule)
        else:
            raise TypeError(rule)

    def getRule(self, index):
        return self.__ruleArray[index]

    def getRuleArray(self):
        return self.__ruleArray

    def setRuleArray(self, RuleArray):
        self.__ruleArray = RuleArray

    def assignOperator(self, RuleSet):
        self.copyInstance(RuleSet)
        return self

    def setParameterForRules(self, name, value):
        for i in self.__ruleArray:
            i.setParameter(name, value)

    def removeRules(self, mode):
        i = 0
        j = 0

        while i < len(self.__ruleArray):
            j = i + 1
            while j < len(self.__ruleArray):
                if self.__ruleArray[i].__eq__(self.__ruleArray[j]):
                    if mode == 0x01:
                        self.__ruleArray[i].increaseSupport(self.__ruleArray[j].getSupport())
                    self.__ruleArray.remove(self.__ruleArray[i])
                    j -= 1
                j += 1
            i += 1

    def removeWeakRules(self, minStrength):
        if type(minStrength) == float:
            newListOfRules = []

            f = lambda x : x.getStrength() < minStrength
            booleanCheckList = list(map(f, self.__ruleArray))

            for i, (x, y) in enumerate(zip(self.__ruleArray, booleanCheckList)):
                if not y:
                    newListOfRules.append(x)

            self.setRuleArray(newListOfRules)
        else:
            raise TypeError(minStrength)

    def computeCosts(self, costArray):
        for i in self.__ruleArray:
            i.computeCost(costArray)

    def computeStrength(self, objectNumber):
        for i in self.__ruleArray:
            i.computeStrength(objectNumber)

    def computeCoverage(self, valuesOfAttr):
        for i in self.__ruleArray:
            i.computeCoverage(valuesOfAttr)

    def computeCertainty(self):
        for i in self.__ruleArray:
            i.computeCertainty()

    def computeSignatures(self):
        for i in self.__ruleArray:
            i.computeSignature()

    def compInhibRules(self, attrValues, inhibRules):
        inhb = 0

        for x in range(len(self.__ruleArray)):
            for n, m in self.__ruleArray[x].getConsequent().items():
                key = n
                value = m

                for k, v in attrValues.items():
                    if k == key:
                        for i, j in v.items():
                            if value != i:
                                inhibRules.append(CRule())

                                for k, v in self.__ruleArray[x].getAntecedent().items():
                                    inhibRules.getRule(inhb).getAntecedent().add(k, v)

                                inhibRules.getRule(inhb).getConsequent().add(key, i)
                                inhibRules.getRule(inhb).setCoverage(self.__ruleArray[x].getCoverage())
                                inhibRules.getRule(inhb).setStrength(self.__ruleArray[x].getStrength())
                                inhibRules.getRule(inhb).setSupport(self.__ruleArray[x].getSupport())
                                inhb += 1

        return inhibRules