from CGlobalState import CGlobalState

class CInformTable(list, CGlobalState):

    def __init__(self):
        self.informationTable = []

    def getInformationTable(self):
        return self.informationTable

    def setInformationTable(self, informationTable):
        if isinstance(informationTable, self.__class__):
            for i in range(len(self.informationTable)):
                del self.informationTable[i]

            for i in range(len(informationTable.getInformationTable())):
                self.informationTable.append(informationTable[i])
        else:
            raise TypeError(informationTable)

    def append(self, globalState):
        if isinstance(globalState, CGlobalState):
            self.informationTable.append(globalState)
        else:
            raise TypeError(globalState)

    def size(self):
        return len(self.informationTable)

    def getObject(self, index):
        return self.informationTable[index]

    def removeIdentObjects(self):
        pass

    def checkIndiscern(self):
        pass

    def loadFromProject(self):
        pass

    def saveToProject(self):
        pass