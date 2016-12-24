import copy
from CImplicant import CImplicant


class CImplArray(list):
    def __init__(self):
        self._implicantArray = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self.getImplicantArray()) == len(other.getImplicantArray()):
                implicantArray = copy.deepcopy(self)
                implicantArray1 = copy.deepcopy(other)

                implicantArray.sort()
                implicantArray1.sort()

                identical = True
                for x, y in zip(implicantArray.getImplicantArray(), implicantArray1.getImplicantArray()):
                    if not x.__eq__(y):
                        identical = False
                        break
                return identical
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.getImplicantArray()))

    def copyInstance(self, implicantArray):
        if isinstance(implicantArray, self.__class__):
            self.clear()

            for i in implicantArray.getImplicantArray():
                self._implicantArray.append(i)
        else:
            raise TypeError(implicantArray)

    def pop(self, index):
        if 0 <= index < len(self._implicantArray):
            return self._implicantArray.pop(index)
        else:
            raise ValueError(index)

    def index(self, cImplicant):
        if isinstance(cImplicant, CImplicant):
            return self._implicantArray.index(cImplicant)
        else:
            raise TypeError(cImplicant)

    def insert(self, index, cImplicant):
        if isinstance(cImplicant, CImplicant):
            self._implicantArray.insert(index, cImplicant)
        else:
            raise TypeError(cImplicant)

    def clear(self):
        self._implicantArray.clear()

    def remove(self, cImplicant):
        if isinstance(cImplicant, CImplicant):
            self._implicantArray.remove(cImplicant)
        else:
            raise TypeError(cImplicant)

    def append(self, cImplicant):
        self._implicantArray.append(cImplicant)

    def copy(self):
        self._implicantArray.copy()

    def size(self):
        return len(self._implicantArray)

    def getImplicant(self, index):
        return self._implicantArray[index]

    def getImplicantArray(self):
        return self._implicantArray

    def sort(self):
        for i in range(len(self._implicantArray) - 1):
            minimum = i
            for j in range(i + 1, len(self._implicantArray)):
                if self.getImplicant(j).count(1) < self.getImplicant(minimum).count(1):
                    minimum = j

            implicant = copy.deepcopy(self.getImplicant(i))
            implicantMinimum = copy.deepcopy(self.getImplicant(minimum))
            self.getImplicant(i).assignOperator(implicantMinimum)
            self.getImplicant(minimum).assignOperator(implicant)

    def minimalize(self):
        i = 0

        while i < len(self._implicantArray):
            j = i + 1
            while j < len(self._implicantArray):
                if self.getImplicant(i).inclusionOperator(self.getImplicant(j)):
                    self.remove(self.getImplicant(j))
                    j -= 1
                j += 1
            i += 1

    def conj2disj(self):
        implicantIndex = 0
        implicantArray = CImplArray()

        if len(self.getImplicantArray()) > 0:
            for i in range(self.getImplicant(0).size()):
                if self.getImplicant(0).test(i):
                    implicantSize = self.getImplicant(0).size()

                    implicantArray.insert(implicantIndex, CImplicant(implicantSize))
                    implicantArray.getImplicant(implicantIndex).setValue(i)
                    implicantIndex += 1

            for i in range(1, len(self.getImplicantArray())):
                implicantArrayCopy = copy.deepcopy(implicantArray)
                secondImplicantArray = implicantArrayCopy.cartesianOperator(self.getImplicant(i))
                implicantArray.assignOperator(secondImplicantArray)

        return implicantArray

    def assignOperator(self, implicantArray):
        if isinstance(implicantArray, self.__class__):
            if not self.__eq__(implicantArray):
                self.clear()
                self.copyInstance(implicantArray)
            return self
        else:
            return self

    def cartesianOperator(self, implicant):
        implicantIndex = 0
        implicantArray = CImplArray()

        for i in range(len(self.getImplicantArray())):
            for j in range(implicant.size()):
                if implicant.test(j):
                    implicantSize = self.getImplicant(i).size()

                    implicantArray.insert(implicantIndex, CImplicant(implicantSize))
                    implicantArray.getImplicant(implicantIndex).assignOperator(self.getImplicant(i))
                    implicantArray.getImplicant(implicantIndex).setValue(j)
                    implicantIndex += 1

        implicantArray.sort()
        implicantArray.minimalize()

        return implicantArray