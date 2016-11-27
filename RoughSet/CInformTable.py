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

    def printSome(self):
        for i in self._informationTable:
            print(i.getDescriptors())

    def removeIdentObjects(self):
        x = self.copy()
        self.clear()
        self._informationTable = list(set(x))

    def checkIndiscern(self, state, attributes):
        indiscernStateInd = -1

        if type(state) == int and type(attributes) == list:
            for i in range(self.size()):
                if self.getObject(i).compareUsingAttributesList(self.getObject(state), attributes):
                    indiscernStateInd = i
                    break

            return indiscernStateInd
        else:
            return indiscernStateInd

    def loadFromProject(self):
        pass

    def saveToProject(self):
        pass