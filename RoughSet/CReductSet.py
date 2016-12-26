from CImplArray import CImplArray
from CReduct import CReduct


class CReductSet:
    def __init__(self):
        self.__reductArray = []

    def append(self, reduct):
        if isinstance(reduct, CReduct):
            self.__reductArray.append(reduct)
        else:
            raise TypeError(reduct)

    def insert(self, index, reduct):
        if isinstance(reduct, CReduct):
            self.__reductArray.insert(index, reduct)
        else:
            raise TypeError(reduct)

    def getReduct(self, index):
        return self.__reductArray[index]

    def getReducts(self):
        return self.__reductArray

    def size(self):
        return len(self.__reductArray)

    def write(self, implArr, reductSize):
        if isinstance(implArr, CImplArray):
            for i in range(implArr.size()):
                self.insert(i, CReduct(reductSize))
                self.getReduct(i).setName(i+1)
                self.getReduct(i).getAttributes().orOperat(implArr.getImplicant(i))
        else:
            raise TypeError(implArr)

    def removeAll(self):
        for i in self.__reductArray:
            del i

    def saveXML(self, File, ISName, NameAttr):
        pass

    def saveXML2(self, pDoc ,redsNodePtr ,attrNames):
        pass

    def loadFromProject(self, redsNodePtr, attrInd):
        pass

    def saveToProject(self, pDoc, pProjNode, attrNames):
        pass