from Bitset import Bitset


class CImplicant(Bitset):
    """ Constructor """
    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        super().__init__(MAX_ATTRIBUTE_NUMBER)
        self.reset()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getBitsetList() == other.getBitsetList()
        else:
            return False

    def __hash__(self):
        return hash(tuple(self.getBitsetList()))

    def getBitsetList(self):
        return super().getBitsetList()

    def count(self, elem):
        return super().count(elem)

    def test(self, index):
        return super().test(index)

    def size(self):
        return super().size()

    def setValue(self, index):
        return super().setValue(index)

    def pop(self, index):
        return super().pop(index)

    def appendString(self, elem):
        return super().appendString(elem)

    def none(self):
        return super().none()

    def flip(self):
        super().flip()

    def all(self):
        return super().all()

    def setBitsetList(self, binaryList):
        super().setBitsetList(binaryList)

    def resetBinaryValue(self, index):
        return super().resetBinaryValue(index)

    def setAll(self):
        super().setAll()

    def toInt(self):
        return super().toInt()

    def getElement(self, index):
        return super().getElement(index)

    def append(self, elem):
        return super().append(elem)

    def reset(self):
        super().reset()

    def remove(self, index):
        return super().remove(index)

    def setValueAtIndex(self, index, elem):
        return super().setValueAtIndex(index, elem)

    def toString(self):
        return super().toString()

    def any(self):
        return super().any()

    def orOperator(self, instance):
        """ OR operator """
        if isinstance(instance, self.__class__):
            """ reversed list """
            classImplicant = self.getBitsetList()[::-1]
            """ reversed list """
            instanceImplicant = instance.getBitsetList()[::-1]

            for x, (i, j) in enumerate(zip(classImplicant, instanceImplicant)):
                value = i | j
                self.setValueAtIndex(x, value)
        else:
            raise TypeError(instance)

    def andOperator(self, instance):
        """ AND operator """
        implicant = CImplicant(instance.size())
        if isinstance(instance, self.__class__):
            """ reversed list """
            classImplicant = self.getBitsetList()[::-1]
            """ reversed list """
            instanceImplicant = instance.getBitsetList()[::-1]

            for x, (i, j) in enumerate(zip(classImplicant, instanceImplicant)):
                value = i & j
                implicant.setValueAtIndex(x, value)
        else:
            raise TypeError(instance)
        return implicant

    def copyInstance(self, instance):
        """ Copy instance with values """
        self.reset()
        self.orOperator(instance)

    def assignOperator(self, instance):
        if self.getBitsetList() != instance.getBitsetList():
            self.reset()
            self.orOperator(instance)
        else:
            return self

    def inclusionOperator(self, instance):
        if self.getBitsetList() == instance.getBitsetList():
            return True

        if self.andOperator(instance).getBitsetList() == self.getBitsetList():
            return True
        else:
            return False

    def intToBinaryString(self, intValue):
        return "{0:b}".format(intValue)

    def binaryStringToList(self, binaryString):
        return list(map(int, binaryString))