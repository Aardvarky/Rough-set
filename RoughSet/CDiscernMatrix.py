from CImplicant import CImplicant


class CDiscernMatrix:

    def __init__(self, dimension=0):
        self.__tab = [[CImplicant() for i in range(dimension)] for j in range(dimension)]

    def saveXML(self, pDoc, pDiscMatrNode, objects, attributeNames):
        pass

    def getTab(self):
        return self.__tab

    def printTab(self):
        for row in self.__tab:
            print(row)