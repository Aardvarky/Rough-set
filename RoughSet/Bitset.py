class Bitset(list):
    def __init__(self, MAX_ATTR_NUMB=0):
        self.__array = [1 for _ in range(MAX_ATTR_NUMB)]

    def append(self, elem):
        if elem == 0 or elem == 1:
            self.__array.append(elem)
        else:
            raise ValueError(elem)

    def set(self, index, elem):
        if elem == 0 or elem == 1:
            if 0 <= index < len(self.__array):
                self.__array[len(self.__array) - index - 1] = elem
            else:
                raise IndexError(index)
        else:
            raise ValueError(elem)

    def setValue(self, index):
        if 0 <= index < len(self.__array):
            self.__array[len(self.__array) - index - 1] = 1
        else:
            raise IndexError(index)

    def remove(self, elem):
        if elem == 0 or elem == 1:
            self.__array.remove(elem)
        else:
            raise ValueError(elem)

    def pop(self, index):
        if 0 <= index < len(self.__array):
            print self.__array.pop(index)
        else:
            raise IndexError(index)

    def index(self, elem):
        if elem == 0 or elem == 1:
            print self.__array.index(elem)
        else:
            raise ValueError(elem)

    def count(self, elem):
        if elem == 0 or elem == 1:
            print self.__array.count(elem)
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

    def getArray(self):
        return self.__array

    def getBitsetArray(self):
        return "".join(map(str, self.__array))