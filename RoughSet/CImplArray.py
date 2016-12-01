from CImplicant import CImplicant


class CImplArray(list):
    def __init__(self):
        self._implicantArray = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            identical = True
            for i, (x, y) in enumerate(zip(self.getImplicantArray(), other.getImplicantArray())):
                if not x.__eq__(y):
                    identical = False
                    break
            return identical
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.getImplicantArray()))

    def copyInstance(self, implicantArray):
        if isinstance(implicantArray, self.__class__):
            self.clear()

            for i in range(implicantArray.size()):
                self._implicantArray.append(implicantArray[i])
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

    def getImplicantArray(self):
        return self._implicantArray

    def sort(self, cmp=None, key=None, reverse=False):
        pass

    def minimalize(self):
        pass

    def conj2disj(self):
        pass

    def assignOperator(self, implicantArray):
        if isinstance(implicantArray, self.__class__):
            if not self.__eq__(implicantArray):
                self.clear()
                self.copyInstance(implicantArray)
            return self
        else:
            return self

    def cartesianOperator(self, cImplicant):
        pass