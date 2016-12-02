class CRuleSet:
    def __init__(self):
        pass

    def copyInstance(self, RuleSet):
        pass

    def assignOperator(self, RuleSet):
        pass

    def setParameterForRules(self, name, value):
        pass

    def removeRules(self, mode):
        pass

    def removeWeakRules(self, minStrength):
        pass

    def computeCosts(self, costArray):
        pass

    def computeStrength(self, objectNumber):
        pass

    def computeCoverage(self, valuesOfAttr):
        pass

    def computeCertainty(self):
        pass

    def computeSignatures(self):
        pass

    def compInhibRules(self, attrValues, inhibRules):
        pass