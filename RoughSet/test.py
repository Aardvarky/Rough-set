from CInformTable import CInformTable
from CGlobalState import CGlobalState
from BasicInformSystem import BasicInformSystem
from CImplicant import CImplicant
from CImplArray import CImplArray
from CRule import CRule
from HashableDict import HashableDict


consequent = HashableDict()
consequent.add(1, 1.0)
consequent.add(2, 2.0)
consequent.add(3, 3.0)

consequent1 = HashableDict()
consequent1.add(1, 1.0)
consequent1.add(2, 2.0)
consequent1.add(3, 3.0)

antecedent = HashableDict()
antecedent.add(1, 1.0)
antecedent.add(2, 2.0)
antecedent.add(3, 3.0)

antecedent1 = HashableDict()
antecedent1.add(1, 1.0)
antecedent1.add(2, 2.0)
antecedent1.add(3, 3.0)

cRule = CRule()
cRule.setConsequent(consequent)
cRule.setAntecedent(antecedent)


cRule1 = CRule()
cRule1.setConsequent(consequent1)
cRule1.setAntecedent(antecedent1)


print(cRule.equalOperator(cRule1))