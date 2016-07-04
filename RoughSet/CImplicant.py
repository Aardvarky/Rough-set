from Bitset import Bitset


class CImplicant(Bitset):
    def __init__(self, MAX_ATTR_NUMB=0):
        Bitset.__init__(self, MAX_ATTR_NUMB)
        self.__bitset = Bitset(MAX_ATTR_NUMB)
        self.__bitset.reset()

    def setValue(self, index):
        self.__bitset.setValue(index)

    def setValuesFromImplicant(self, implicant):
        self.__bitset.reset()

        if self.__eq__(implicant):
            array = implicant.getBitsetArray()
            j = 0

            for i in range(self.__bitset.size()):
                self.__bitset.set(i, int(array[j]))
                j += 1

    def setValues(self, implicant):
        self.__bitset.reset()
        j = 0

        if type(implicant) is str and len(implicant) == self.__bitset.size():
            for i in range(self.__bitset.size()):
                self.__bitset.set(i, int(implicant[j]))
                j += 1
        else:
            raise ValueError(implicant)

    def getBitsetArray(self):
        return self.__bitset.getBitsetArray()

    def __eq__(self, implicant):
        if isinstance(implicant, self.__class__):
            return self.__dict__ == implicant.__dict__
        else:
            return False