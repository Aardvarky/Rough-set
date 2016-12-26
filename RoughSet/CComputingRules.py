import copy
from CRule import CRule
from CRuleSet import CRuleSet
from CImplicant import CImplicant
from CImplArray import CImplArray


class CComputingRules:
    def __init__(self):
        super().__init__()

    def minimDiscFunc(self, implArrIn):

        implArrOut = CImplArray()

        for i in range(implArrIn.size()):
            if implArrIn.getImplicant(i).none():
                return

        implArrIn.sort()
        implArrIn.minimalize()

        # implArrInCopy = copy.deepcopy(implArrIn)
        # implArrInCopy.conj2disj()
        #
        # implArrOut.assignOperator(implArrInCopy)

        implArrOut.assignOperator(implArrIn.conj2disj())

        implArrOut.sort()
        implArrOut.minimalize()

        return implArrOut

    def comRules(self, conAttr, decAttr, objectNumber, objects, attributeNumber):
        ruleSet = CRuleSet()

        ruleNumber = 0
        implNumber = 0

        for o in range(objectNumber):
            implicents = CImplArray()
            implicants = CImplArray()

            implNumber = 0

            for o2 in range(objectNumber):
                if o2 != o:
                    decValue1 = objects.getObject(o).getDescriptors().get(decAttr)
                    decValue2 = objects.getObject(o2).getDescriptors().get(decAttr)

                    if decValue1 != decValue2:
                        implicents.insert(implNumber, CImplicant(attributeNumber))

                        for k in range(len(conAttr)):
                            condValue1 = objects.getObject(o).getDescriptors().get(conAttr[k])
                            condValue2 = objects.getObject(o2).getDescriptors().get(conAttr[k])

                            if condValue1 != condValue2:
                                implicents.getImplicant(implNumber).setValue(conAttr[k])
                        implNumber += 1

            if implicents.size() != 0:
                implicants.assignOperator(self.minimDiscFunc(implicents))
            else:
                implicants.append(CImplicant(0))

            for i in range(implicants.size()):
                ruleSet.insert(ruleNumber, CRule())
                for j in range(implicants.getImplicant(i).size()):
                    if implicants.getImplicant(i).test(j):
                        attrValue = objects.getObject(o).getDescriptors().get(j)
                        ruleSet.getRule(ruleNumber).getAntecedent().add(j, attrValue)

                attrValue = objects.getObject(o).getDescriptors().get(decAttr)
                ruleSet.getRule(ruleNumber).getConsequent().add(decAttr, attrValue)
                ruleNumber += 1

        return ruleSet