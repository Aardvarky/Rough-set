from HashableDict import HashableDict
from Bitset import Bitset


class CRule:
    def __init__(self):
        self.__antecedent = HashableDict()
        self.__consequent = HashableDict()

        self.__cost = 0.0
        self.__support = 1
        self.__antSupport = 1
        self.__strength = 0.0
        self.__coverage = 0.0
        self.__certainty = 1.0

        self.__parameters = HashableDict()
        self.__signature = Bitset(64)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self.getAntecedent()) == len(other.getAntecedent()) \
                    and len(self.getConsequent()) == len(other.getConsequent()):
                if self.getAntecedent().__eq__(other.getAntecedent()) \
                        and self.getConsequent().__eq__(other.getConsequent()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def getAntecedent(self):
        return self.__antecedent

    def setAntecedent(self, antecedent):
        if isinstance(antecedent, HashableDict):
            self.__antecedent = antecedent
        else:
            raise TypeError(antecedent)

    def getConsequent(self):
        return self.__consequent

    def setConsequent(self, consequent):
        if isinstance(consequent, HashableDict):
            self.__consequent = consequent
        else:
            raise TypeError(consequent)

    def setParameter(self, name, value):
        if type(name) == str and type(value) == str:
            self.__parameters.add(name, value)
        else:
            raise TypeError(name, value)

    def getParameter(self, name):
        return self.__parameters[name]

    def getParameters(self):
        return self.__parameters

    def computeCost(self, costArray):
        for key in self.__antecedent.keys():
            self.__cost += costArray[key]

    def setSupport(self, value):
        self.__support = value

    def getSupport(self):
        return self.__support

    def increaseSupport(self, value):
        self.__support += value

    def increaseAntSupport(self, value):
        self.__antSupport += value

    def setStrength(self, value):
        self.__strength = value

    def getStrength(self):
        return self.__strength

    def computeStrength(self, objectNumber):
        self.__strength = float(self.__support) / float(objectNumber)

    def setCoverage(self, value):
        self.__coverage = value

    def getCoverage(self):
        return self.__coverage

    def computeCoverage(self, valuesOfAttr):
        count = 0

        for key, value in self.__consequent.items():
            if valuesOfAttr.get(key):
                valueOfAttribute = valuesOfAttr.get(key)
                if valueOfAttribute.get(value):
                    count = valueOfAttribute.get(value)
                else:
                    continue
            else:
                continue

        self.__coverage = float(self.__support) / float(count)

    def getCertainty(self):
        return self.__certainty

    def computeCertainty(self):
        self.__certainty = float(self.__support) / float(self.__antSupport)

    def computeSignature(self):
        self.__signature.reset()

        for key in self.__antecedent.keys():
            self.__signature.setValue(key)

        for key in self.__consequent.keys():
            self.__signature.setValue(key)

    def checkAttribute(self, index):
        return self.__signature.test(index)

    def equalOperator(self, rule):
        if isinstance(rule, self.__class__):
            return self.__eq__(rule)
        else:
            raise TypeError(rule)