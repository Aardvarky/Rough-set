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

    def getReduct(self, index):
        return self.__reductArray[index]

    def write(self, implArr, reductSize):
        if isinstance(implArr, CImplArray):
            for i in range(implArr.size()):
                self.append(CReduct(reductSize))
                self.getReduct(i).setName(i+1)
                #TODO
            else:
                raise TypeError(implArr)

    def saveXML(self, File, ISName, NameAttr):
        pass

    def saveXML2(self, pDoc ,redsNodePtr ,attrNames):
        pass

    def loadFromProject(self, redsNodePtr, attrInd):
        pass

    def saveToProject(self, pDoc, pProjNode, attrNames):
        pass