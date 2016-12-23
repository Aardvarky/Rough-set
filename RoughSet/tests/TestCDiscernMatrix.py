from CDiscernMatrix import CDiscernMatrix
from CImplicant import CImplicant

print("--------------dimension--------------------------")

dimension = 4

print(dimension)

print("--------------attribute number-------------------")
attributeNumer = 4

print(attributeNumer)

print("--------------Creating matrix--------------------")

matrix = [[CImplicant(attributeNumer) for i in range(dimension)] for j in range(dimension)]

print(matrix)

print("--------------Creating disc matrix---------------")

firstCDiscernMatrix = CDiscernMatrix(4, 4)
firstCDiscernMatrix.printTab()

print("--------------get matrix-------------------------")

print(firstCDiscernMatrix.getMatrix())

print("--------------set matrix-------------------------")

firstCDiscernMatrix.setMatrix(matrix)

firstCDiscernMatrix.printTab()

print("--------------get implicant from matrix----------")

firstCDiscernMatrix.getImplicant(0, 0)

print(firstCDiscernMatrix.getImplicant(0, 0).getBitsetList())

print("--------------print matrix-----------------------")

firstCDiscernMatrix.printTab()