from Bitset import Bitset
import copy

class CImplicant(Bitset):
    """ Constructor """
    def __init__(self, MAX_ATTRIBUTE_NUMBER=0):
        super().__init__(MAX_ATTRIBUTE_NUMBER)
        self.reset()

    def __eq__(self, other):
        """ Equal method """
        return self.__dict__ == other.__dict__

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
        if not self.__eq__(instance):
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