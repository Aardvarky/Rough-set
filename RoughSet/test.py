from CInformTable import CInformTable
from CGlobalState import CGlobalState
from BasicInformSystem import BasicInformSystem
from CImplicant import CImplicant
from CImplArray import CImplArray
from CRule import CRule
from HashableDict import HashableDict


lista = [1.1, 1.2, 1.1, 1.1]

hashableDict = HashableDict()
hashableDict.add(1, 1.1)
hashableDict.add(2, 2.1)
hashableDict.add(3, 3.1)


cRule = CRule()
cRule.setAntecedent(hashableDict)
cRule.computeCost(lista)