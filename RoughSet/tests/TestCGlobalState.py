from CGlobalState import CGlobalState
from HashableDict import HashableDict
from Bitset import Bitset

print("--------------Creating object---------------------")

firstGlobalState = CGlobalState()
print(firstGlobalState.getDescriptors())

print("--------------Add descriptor----------------------")

firstGlobalState.addDescriptor(1, 1.0)
print(firstGlobalState.getDescriptors())

print("--------------get attribute value-----------------")

print(firstGlobalState.getAttributeValue(1))

print("--------------set and get descriptors-------------")

fistHashableDict = HashableDict()
fistHashableDict.add(2, 2.0)

firstGlobalState.setDescriptors(fistHashableDict)

print(firstGlobalState.getDescriptors())

print("--------------get and set name--------------------")

firstGlobalState.setName("Name")

print(firstGlobalState.getName())

print("--------------creating second global state--------")

secondGlobalState = CGlobalState()
secondGlobalState.addDescriptor(1, 1.1)
secondGlobalState.addDescriptor(3, 3.0)

print(secondGlobalState.getDescriptors())

print("--------------comparing using attribute list------")

print(firstGlobalState.compareUsingAttributesList(secondGlobalState, [1, 2]))

fistBitset = Bitset(2)
fistBitset.setAll()

print("--------------comparing using bitset--------------")

print(firstGlobalState.compareUsingBitset(secondGlobalState, fistBitset))

print("--------------comparing using attribute-----------")

print(firstGlobalState.compareUsingAttribute(secondGlobalState, 1))

print("--------------assign operator---------------------")

thirdGlobalState = firstGlobalState.assignOperator(secondGlobalState)
print(thirdGlobalState.getDescriptors())

print("--------------comparison operator----------------")

print(firstGlobalState.comparasionOperator(secondGlobalState))