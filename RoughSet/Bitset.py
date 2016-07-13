class Bitset(list):
    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        self._array = [0 for _ in range(MAX_ATTRIBUTE_NUMBER)]

    def append(self, elem):
        binaryValue = elem
        if binaryValue == 0 or binaryValue == 1:
            self._array.insert(0, binaryValue)
        else:
            raise ValueError(elem)

    def appendInt(self, elem):
        if elem == 0 or elem == 1:
            self._array.insert(0, elem)
        else:
            raise ValueError(elem)

    def appendString(self, elem):
        if len(elem) == 1:
            binaryValue = int(elem)
            if binaryValue == 0 or binaryValue == 1:
                self._array.insert(0, binaryValue)
            else:
                raise ValueError(binaryValue)
        else:
            raise IndexError(elem)

    def setValue(self, index):
        if 0 <= index < len(self._array):
            self._array[len(self._array) - index - 1] = 1
        else:
            raise IndexError(index)

    def setValueAtIndex(self, index, elem):
        if elem == 0 or elem == 1:
            if 0 <= index < len(self._array):
                self._array[len(self._array) - index - 1] = elem
            else:
                raise IndexError(index)
        else:
            raise ValueError(elem)

    def setAll(self):
        for i in range(len(self._array)):
            self._array[i] = 1

    def remove(self, index):
        if 0 <= index < len(self._array):
            del self._array[index]
        else:
            raise IndexError(index)

    def pop(self, index):
        if 0 <= index < len(self._array):
            return self._array.pop(index)
        else:
            raise IndexError(index)

    def count(self, elem):
        if elem == 0 or elem == 1:
            return self._array.count(elem)
        else:
            raise ValueError(elem)

    def flip(self):
        self._array.reverse()

    def reset(self):
        for i in range(len(self._array)):
            self._array[i] = 0

    def resetBinaryValue(self, index):
        if 0 <= index < len(self._array):
            for i in range(len(self._array)):
                if i == (len(self._array) - index - 1):
                    self._array[i] = 0
        else:
            raise IndexError(index)

    def size(self):
        return len(self._array)

    def test(self, index):
        if 0 <= index < len(self._array):
            if self._array[index] == 0:
                return False
            else:
                return True
        else:
            raise IndexError(index)

    def any(self):
        if 1 in self._array:
            return True
        else:
            return False

    def none(self):
        if not 1 in self._array:
            return True
        else:
            return False

    def all(self):
        if not 0 in self._array:
            return True
        else:
            return False

    def getBitsetList(self):
        return self._array

    def setBitsetList(self, binaryList):
        self._array = binaryList

    def getElement(self, index):
        if 0 <= index < len(self._array):
            return self._array[index]
        else:
            raise IndexError(index)

    def toString(self):
        return "".join(map(str, self._array))

    def toInt(self):
        return int(self.toString(), 2)