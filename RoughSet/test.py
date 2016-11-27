from Bitset import Bitset
from CInformTable import CInformTable
from CGlobalState import CGlobalState

lista = [1,2]
lista1 = [2,2]

inf = CInformTable()
inf1 = CInformTable()


state = CGlobalState()
state.setName("global state 1")
state.setDescriptors({1: 1.1, 2: 1.2, 3: 1.3, 4: 1.4})

state1 = CGlobalState()
state1.setName("global state 2")
state1.setDescriptors({1: 2.1, 2: 2.2, 3: 2.3, 4: 2.4})

state2 = CGlobalState()
state2.setName("global state 3")
state2.setDescriptors({1: 3.1, 2: 3.2, 3: 3.3, 4: 3.4})

state3 = CGlobalState()
state3.setName("global state 4")
state3.setDescriptors({1: 1.1, 2: 1.2, 3: 1.3, 4: 1.4})

state4 = CGlobalState()
state4.setName("global state 2")
state4.setDescriptors({1: 2.1, 2: 2.2, 3: 2.3, 4: 2.4})


inf.append(state)
inf.append(state1)
inf.append(state2)
inf.append(state3)
inf.append(state4)

# print(inf.getInformationTable())
inf.printSome()
inf.removeIdentObjects()
print()
inf.printSome()
# print(inf.getInformationTable())