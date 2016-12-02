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

val = HashableDict()
val.add(1.0, 1)
val.add(2.0, 2)
val.add(3.0, 3)

val1 = HashableDict()
val1.add(1.0, 4)
val1.add(2.0, 5)
val1.add(3.0, 6)

val2 = HashableDict()
val2.add(1.0, 7)
val2.add(2.0, 8)
val2.add(3.0, 9)

disc = HashableDict()
disc.add(1, val)
disc.add(2, val1)
disc.add(3, val2)

cRule = CRule()
cRule.setConsequent(consequent)
cRule.computeCoverage(disc)