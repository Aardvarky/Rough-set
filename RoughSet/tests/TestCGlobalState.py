from CGlobalState import CGlobalState
from HashableDict import HashableDict
from Bitset import Bitset

fistGlobalState = CGlobalState()

fistGlobalState.addDescriptor(1, 1.0)

fistGlobalState.getAttributeValue(1)

fistHashableDict = HashableDict()
fistHashableDict.add(2, 2.0)

fistGlobalState.getDescriptors()
fistGlobalState.setDescriptors(fistHashableDict)

fistGlobalState.getName()
fistGlobalState.setName("Name")

secondGlobalState = CGlobalState()
secondGlobalState.addDescriptor(1, 1.1)
secondGlobalState.addDescriptor(3, 3.0)

fistGlobalState.compareUsingAttributesList(secondGlobalState, [1, 2])

fistBitset = Bitset(2)
fistBitset.setAll()

fistGlobalState.compareUsingBitset(secondGlobalState, fistBitset)
fistGlobalState.compareUsingAttribute(secondGlobalState, 1)

fistGlobalState.assignOperator(secondGlobalState)

fistGlobalState.comparasionOperator(secondGlobalState)
