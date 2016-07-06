class Bitset(list):
    def __init__(self, MAX_ATTR_NUMB=0):
        self.__array = [0 for _ in range(MAX_ATTR_NUMB)]

    def append(self, elem):
        binaryValue = elem
        if binaryValue == 0 or binaryValue == 1:
            self.__array.append(binaryValue)
        else:
            raise ValueError(elem)

    def appendInt(self, elem):
        if elem == 0 or elem == 1:
            self.__array.append(elem)
        else:
            raise ValueError(elem)

    def appendString(self, elem):
        if len(elem) == 1:
            binaryValue = int(elem)
            if binaryValue == 0 or binaryValue == 1:
                self.__array.append(binaryValue)
            else:
                raise ValueError(binaryValue)
        else:
            raise IndexError(elem)

    def setValue(self, index):
        if 0 <= index < len(self.__array):
            self.__array[len(self.__array) - index - 1] = 1
        else:
            IndexError(index)

    def setValueAtIndex(self, index, elem):
        if elem == 0 or elem == 1:
            if 0 <= index < len(self.__array):
                self.__array[len(self.__array) - index - 1] = elem
            else:
                raise IndexError(index)
        else:
            raise ValueError(elem)

    def setAll(self):
        for i in range(len(self.__array)):
            self.__array[i] = 1

    def setValue(self, index):
        if 0 <= index < len(self.__array):
            self.__array[len(self.__array) - index - 1] = 1
        else:
            raise IndexError(index)

    def remove(self, index):
        if 0 <= index < len(self.__array):
            del self.__array[index]
        else:
            raise IndexError(index)

    def pop(self, index):
        if 0 <= index < len(self.__array):
            return self.__array.pop(index)
        else:
            raise IndexError(index)

    def count(self, elem):
        if elem == 0 or elem == 1:
            return self.__array.count(elem)
        else:
            raise ValueError(elem)

    def flip(self):
        self.__array.reverse()

    def reset(self):
        for i in range(len(self.__array)):
            self.__array[i] = 0

    def resetBinaryValue(self, index):
        if 0 <= index < len(self.__array):
            for i in range(len(self.__array)):
                if i == (len(self.__array) - index - 1):
                    self.__array[i] = 0
        else:
            raise IndexError(index)

    def size(self):
        return len(self.__array)

    def test(self, index):
        if 0 <= index < len(self.__array):
            if self.__array[index] == 0:
                return False
            else:
                return True
        else:
            raise IndexError(index)

    def any(self):
        if 1 in self.__array:
            return True
        else:
            return False

    def none(self):
        if not 1 in self.__array:
            return True
        else:
            return False

    def all(self):
        if not 0 in self.__array:
            return True
        else:
            return False

    def getBitsetArray(self):
        return self.__array

    def getElement(self, index):
        if 0 <= index < len(self.__array):
            return self.__array[index]
        else:
            raise IndexError(index)

    def toString(self):
        return "".join(map(str, self.__array))

    def toInt(self):
        return int(self.toString(), 2)
