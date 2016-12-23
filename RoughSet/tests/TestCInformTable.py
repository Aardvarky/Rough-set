from CGlobalState import CGlobalState
from CInformTable import CInformTable
from HashableDict import HashableDict

print("--------------first hashable dict-------------------------")
print("--------------flip method---------------------------------")


fistHashableDict = HashableDict()
fistHashableDict.add(1, 1.0)
fistHashableDict.add(2, 2.0)
fistHashableDict.add(3, 3.0)
fistHashableDict.add(4, 4.0)

print(fistHashableDict)

print("--------------second hashable dict------------------------")

secondHashableDict = HashableDict()
secondHashableDict.add(1, 5.0)
secondHashableDict.add(2, 6.0)
secondHashableDict.add(3, 7.0)
secondHashableDict.add(4, 8.0)

print(secondHashableDict)

print("--------------third hashable dict------------------------")

thirdHashableDict = HashableDict()
thirdHashableDict.add(1, 1.0)
thirdHashableDict.add(2, 2.0)
thirdHashableDict.add(3, 3.0)
thirdHashableDict.add(4, 4.0)

print(thirdHashableDict)

print("--------------fourth hashable dict-----------------------")

fourthHashableDict = HashableDict()
fourthHashableDict.add(1, 5.0)
fourthHashableDict.add(2, 6.0)
fourthHashableDict.add(3, 7.0)
fourthHashableDict.add(4, 8.0)

print(fourthHashableDict)

print("--------------fifth hashable dict------------------------")

fifthHashableDict = HashableDict()
fifthHashableDict.add(1, 10.0)
fifthHashableDict.add(2, 11.0)
fifthHashableDict.add(3, 12.0)
fifthHashableDict.add(4, 13.0)

print(fifthHashableDict)

print("--------------sixth hashable dict------------------------")

sixthHashableDict = HashableDict()
sixthHashableDict.add(1, 14.0)
sixthHashableDict.add(2, 15.0)
sixthHashableDict.add(3, 16.0)
sixthHashableDict.add(4, 17.0)

print(sixthHashableDict)

print("--------------seventh hashable dict----------------------")

seventhHashableDict = HashableDict()
seventhHashableDict.add(1, 10.0)
seventhHashableDict.add(2, 11.0)
seventhHashableDict.add(3, 12.0)
seventhHashableDict.add(4, 13.0)

print(seventhHashableDict)

print("--------------eighth hashable dict-----------------------")

eighthHashableDict = HashableDict()
eighthHashableDict.add(1, 14.0)
eighthHashableDict.add(2, 15.0)
eighthHashableDict.add(3, 16.0)
eighthHashableDict.add(4, 17.0)

print(eighthHashableDict)

print("--------------first global state-------------------------")

firstCGlobalState = CGlobalState()
firstCGlobalState.setName("G1")
firstCGlobalState.setDescriptors(fistHashableDict)

print(firstCGlobalState)

print("--------------second global state------------------------")

secondCGlobalState = CGlobalState()
secondCGlobalState.setName("G2")
secondCGlobalState.setDescriptors(secondHashableDict)

print(secondCGlobalState)

print("--------------third global state-------------------------")

thirdCGlobalState = CGlobalState()
thirdCGlobalState.setName("G3")
thirdCGlobalState.setDescriptors(thirdHashableDict)

print(thirdCGlobalState)

print("--------------fourth global state------------------------")

fourthCGlobalState = CGlobalState()
fourthCGlobalState.setName("G4")
fourthCGlobalState.setDescriptors(fourthHashableDict)

print(fourthCGlobalState)

print("--------------fifth global state-------------------------")

fifthCGlobalState = CGlobalState()
fifthCGlobalState.setName("G5")
fifthCGlobalState.setDescriptors(fifthHashableDict)

print(fifthCGlobalState)

print("--------------sixth global state-------------------------")

sixthCGlobalState = CGlobalState()
sixthCGlobalState.setName("G6")
sixthCGlobalState.setDescriptors(sixthHashableDict)

print(sixthCGlobalState)

print("--------------seventh global state-----------------------")

seventhCGlobalState = CGlobalState()
seventhCGlobalState.setName("G7")
seventhCGlobalState.setDescriptors(seventhHashableDict)

print(seventhCGlobalState)

print("--------------eighth global state------------------------")

eighthCGlobalState = CGlobalState()
eighthCGlobalState.setName("G8")
eighthCGlobalState.setDescriptors(eighthHashableDict)

print(eighthCGlobalState)

print("--------------first inform table-------------------------")

firstCInformTable = CInformTable()
firstCInformTable.append(firstCGlobalState)
firstCInformTable.append(secondCGlobalState)
firstCInformTable.append(thirdCGlobalState)
firstCInformTable.append(fourthCGlobalState)

print(firstCInformTable.getInformationTable())

print("--------------second global state------------------------")

secondCInformTable = CInformTable()
secondCInformTable.append(fifthCGlobalState)
secondCInformTable.append(sixthCGlobalState)
secondCInformTable.append(seventhCGlobalState)
secondCInformTable.append(eighthCGlobalState)

print(secondCInformTable.getInformationTable())

print("--------------index of global state----------------------")

print(firstCInformTable.index(firstCGlobalState))
print(secondCInformTable.index(fifthCGlobalState))

print("--------------insert global state------------------------")

firstCInformTable.insert(4, fifthCGlobalState)

print(firstCInformTable.getInformationTable())

secondCInformTable.insert(4, firstCGlobalState)

print(secondCInformTable.getInformationTable())

print("--------------pop global state---------------------------")

print(firstCInformTable.pop(4))
print(secondCInformTable.pop(4))

print("--------------remove global state------------------------")

firstCInformTable.remove(fourthCGlobalState)

print(firstCInformTable.getInformationTable())

secondCInformTable.remove(eighthCGlobalState)

print(secondCInformTable.getInformationTable())

print("--------------size global state--------------------------")

firstCInformTable.size()
secondCInformTable.size()

print("--------------get object global state--------------------")

print(firstCInformTable.getObject(0))
print(secondCInformTable.getObject(0))

print("--------------get information table global state---------")

print(firstCInformTable.getInformationTable())
print(secondCInformTable.getInformationTable())

print("--------------remove ident objects global state----------")

firstCInformTable.removeIdentObjects()

print(firstCInformTable.getInformationTable())

secondCInformTable.removeIdentObjects()

print(secondCInformTable.getInformationTable())

print("--------------check indiscern global state----------------")

firstCInformTable.checkIndiscern(1, [1, 2, 3, 4])
secondCInformTable.checkIndiscern(0, [1, 2, 3, 4])

print("--------------copy inform table---------------------------")

firstCInformTable.copy()
secondCInformTable.copy()

print("--------------print inform table--------------------------")

firstCInformTable.printSome()
secondCInformTable.printSome()

print("--------------copy instance inform table------------------")

firstCInformTable.copyInstance(secondCInformTable)

print(firstCInformTable.printSome())

print("--------------clear inform table--------------------------")

firstCInformTable.clear()

print(firstCInformTable.printSome())

secondCInformTable.clear()

print(secondCInformTable.printSome())