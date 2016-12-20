import copy


class CComputingRules:
    def __init__(self):
        super().__init__()

    def minimDiscFunc(self, implArrIn, implArrOut):

        for i in range(implArrIn.size()):
            if implArrIn.getImplicant(i).none():
                return

        implArrIn.sort()
        implArrIn.minimalize()

        implArrInCopy = copy.deepcopy(implArrIn)
        implArrInCopy.conj2disj()

        implArrOut.assignOperator(implArrInCopy)

        implArrOut.sort()
        implArrOut.minimalize()

        return implArrOut


    def comRules(self, conAttr, decAttr, objectNumber, objects):
        pass