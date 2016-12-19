from CDiscernMatrix import CDiscernMatrix
from CImplicant import CImplicant


dimension = 4
attributeNumer = 4
matrix = [[CImplicant(attributeNumer) for i in range(dimension)] for j in range(dimension)]

firstCDiscernMatrix = CDiscernMatrix(4, 4)
firstCDiscernMatrix.getMatrix()
firstCDiscernMatrix.setMatrix(matrix)
firstCDiscernMatrix.getImplicant(0, 0)
firstCDiscernMatrix.printTab()