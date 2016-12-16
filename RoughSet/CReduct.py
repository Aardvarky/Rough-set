from Bitset import Bitset


class CReduct:
    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        self.__attributes = Bitset(MAX_ATTRIBUTE_NUMBER)
        self.__attributes.reset()
        self.__name = ""
        self.__choice = False

    def setName(self, index):
        self.__name = "R" + str(index)

    def setChoice(self, boolean):
        self.__choice = boolean

    def isChosen(self):
        return self.__choice

    def getName(self):
        return self.__name

    def getAttributes(self):
        return self.__attributes

    def getAttributesAsInt(self):
        return self.__attributes.toInt()

    def loadFromProject(self, redNodePtr, attrInd):
        pass

    def saveToProject(self, pDoc , pRedNode , attrNames):
        pass