from Bitset import Bitset
from CInformTable import CInformTable
from CGlobalState import CGlobalState
lista = [1,2]
lista1 = [2,2]

inf = CInformTable()
inf1 = CInformTable()


state = CGlobalState()
state.setName("global state 1")
state.setDescriptors({1: 2.3, 2: 2.4, 3: 2.5, 4: 2.6})


state1 = CGlobalState()
state1.setName("global state 2")
state1.setDescriptors({1: 2.4, 2: 2.5, 3: 2.6, 4: 2.7})

inf.append(state)
inf1.append(state1)

inf.setInformationTable(inf1)
print(inf.getInformationTable())