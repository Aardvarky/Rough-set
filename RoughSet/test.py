from Bitset import Bitset
from CInformTable import CInformTable
from CGlobalState import CGlobalState
from CDiscernMatrix import CDiscernMatrix
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

state2 = CGlobalState()
state2.setName("global state 3")
state2.setDescriptors({1: 2.4, 2: 2.5, 3: 2.6, 4: 2.7})


inf.append(state)
inf.append(state1)
inf.append(state2)