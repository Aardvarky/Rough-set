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
        self.__strength = float(self.__support)/float(objectNumber)

    def setCoverage(self, value):
        self.__coverage = value

    def getCoverage(self):
        return self.__coverage

    def computeCoverage(self):
        """ TODO """

    def getCertainty(self):
        return self.__certainty

    def computeCertainty(self):
        self.__certainty = float(self.__support) / float(self.__antSupport)

    def computeSignature(self):
        """ TODO """

    def checkAttribute(self, index):
        return self.__signature.test(index)

