from Bitset import Bitset

class CImplicant(Bitset):
    def __init__(self, MAX_ATTR_NUMB=0):
        super().__init__(MAX_ATTR_NUMB)
        self.reset()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def bitwiseOrOperator(self, instance):
        if isinstance(instance, self.__class__):
            implicantIntValue = self.toInt()
            instanceIntValue = instance.toInt()
            intValue = implicantIntValue | instanceIntValue
            binaryString = self.intToBinaryString(intValue)
            self.setBitsetList(self.binaryStringToList(binaryString))
        else:
            raise TypeError(instance)

    def copyInstance(self, instance):
        self.reset()
        self.bitwiseOrOperator(instance)

    def assignImplicantOperator(self, instance):
        if not self.__eq__(instance):
            self.reset()
            self.bitwiseOrOperator(instance)
        else:
            return self.getBitsetList()

    def inclusionImplicantOperator(self, instance):
        if self.toInt() <= instance.toInt():
            return True
        else:
            return False

    def intToBinaryString(self,intValue):
        return "{0:b}".format(intValue)

    def binaryStringToList(self, binaryString):
        return list(map(int, binaryString))