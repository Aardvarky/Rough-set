from CImplicant import CImplicant


class CDiscernMatrix:

    def __init__(self, dimension=0, attributeNumer=0):
        self.__matrix = [[CImplicant(attributeNumer) for i in range(dimension)] for j in range(dimension)]

    def saveXML(self, pDoc, pDiscMatrNode, objects, attributeNames):
        pass

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix

    def getImplicant(self, i, j):
        return self.__matrix[i][j]

    def printTab(self):
        for row in self.__matrix:
            for cell in row:
                print(repr(cell.getBitsetList()).rjust(3), end=' ')
            print()