from CGlobalState import CGlobalState


class CInformTable(list):

    def __init__(self):
        self._informationTable = []

    def append(self, globalState):
        if isinstance(globalState, CGlobalState):
            self._informationTable.append(globalState)
        else:
            raise TypeError(globalState)

    def index(self, globalState):
        if isinstance(globalState, CGlobalState):
            return self._informationTable.index(globalState)
        else:
            raise TypeError(globalState)

    def insert(self, index, globalState):
        if isinstance(globalState, CGlobalState):
            self._informationTable.insert(index, globalState)
        else:
            raise TypeError(globalState)

    def pop(self, index):
        return self._informationTable.pop(index)

    def remove(self, globalState):
        if isinstance(globalState, CGlobalState):
            self._informationTable.remove(globalState)
        else:
            raise TypeError(globalState)

    def clear(self):
        self._informationTable.clear()

    def copy(self):
        return self._informationTable.copy()

    def copyInstance(self, informationTable):
        if isinstance(informationTable, self.__class__):
            self.clear()

            for i in range(informationTable.size()):
                self._informationTable.append(informationTable.getObject(i))
        else:
            raise TypeError(informationTable)

    def size(self):
        return len(self._informationTable)

    def getObject(self, index):
        return self._informationTable[index]

    def getInformationTable(self):
        return self._informationTable

    def removeIdentObjects(self):
        pass

    def checkIndiscern(self):
        pass

    def loadFromProject(self):
        pass

    def saveToProject(self):
        pass