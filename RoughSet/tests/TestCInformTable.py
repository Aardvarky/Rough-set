from CGlobalState import CGlobalState
from CInformTable import CInformTable
from HashableDict import HashableDict


fistHashableDict = HashableDict()
fistHashableDict.add(1, 1.0)
fistHashableDict.add(2, 2.0)
fistHashableDict.add(3, 3.0)
fistHashableDict.add(4, 4.0)

secondHashableDict = HashableDict()
secondHashableDict.add(1, 5.0)
secondHashableDict.add(2, 6.0)
secondHashableDict.add(3, 7.0)
secondHashableDict.add(4, 8.0)

thirdHashableDict = HashableDict()
thirdHashableDict.add(1, 1.0)
thirdHashableDict.add(2, 2.0)
thirdHashableDict.add(3, 3.0)
thirdHashableDict.add(4, 4.0)

fourthHashableDict = HashableDict()
fourthHashableDict.add(1, 5.0)
fourthHashableDict.add(2, 6.0)
fourthHashableDict.add(3, 7.0)
fourthHashableDict.add(4, 8.0)

fifthHashableDict = HashableDict()
fifthHashableDict.add(1, 10.0)
fifthHashableDict.add(2, 11.0)
fifthHashableDict.add(3, 12.0)
fifthHashableDict.add(4, 13.0)

sixthHashableDict = HashableDict()
sixthHashableDict.add(1, 14.0)
sixthHashableDict.add(2, 15.0)
sixthHashableDict.add(3, 16.0)
sixthHashableDict.add(4, 17.0)

seventhHashableDict = HashableDict()
seventhHashableDict.add(1, 10.0)
seventhHashableDict.add(2, 11.0)
seventhHashableDict.add(3, 12.0)
seventhHashableDict.add(4, 13.0)

eighthHashableDict = HashableDict()
eighthHashableDict.add(1, 14.0)
eighthHashableDict.add(2, 15.0)
eighthHashableDict.add(3, 16.0)
eighthHashableDict.add(4, 17.0)

firstCGlobalState = CGlobalState()
firstCGlobalState.setName("G1")
firstCGlobalState.setDescriptors(fistHashableDict)

secondCGlobalState = CGlobalState()
secondCGlobalState.setName("G2")
secondCGlobalState.setDescriptors(secondHashableDict)

thirdCGlobalState = CGlobalState()
thirdCGlobalState.setName("G3")
thirdCGlobalState.setDescriptors(thirdHashableDict)

fourthCGlobalState = CGlobalState()
fourthCGlobalState.setName("G4")
fourthCGlobalState.setDescriptors(fourthHashableDict)

fifthCGlobalState = CGlobalState()
fifthCGlobalState.setName("G5")
fifthCGlobalState.setDescriptors(fifthHashableDict)

sixthCGlobalState = CGlobalState()
sixthCGlobalState.setName("G6")
sixthCGlobalState.setDescriptors(sixthHashableDict)

seventhCGlobalState = CGlobalState()
seventhCGlobalState.setName("G7")
seventhCGlobalState.setDescriptors(seventhHashableDict)

eighthCGlobalState = CGlobalState()
eighthCGlobalState.setName("G8")
eighthCGlobalState.setDescriptors(eighthHashableDict)

firstCInformTable = CInformTable()
firstCInformTable.append(firstCGlobalState)
firstCInformTable.append(secondCGlobalState)
firstCInformTable.append(thirdCGlobalState)
firstCInformTable.append(fourthCGlobalState)

secondCInformTable = CInformTable()
secondCInformTable.append(fifthCGlobalState)
secondCInformTable.append(sixthCGlobalState)
secondCInformTable.append(seventhCGlobalState)
secondCInformTable.append(eighthCGlobalState)

firstCInformTable.index(firstCGlobalState)
secondCInformTable.index(fifthCGlobalState)

firstCInformTable.insert(4, fifthCGlobalState)
secondCInformTable.insert(4, firstCGlobalState)

firstCInformTable.pop(4)
secondCInformTable.pop(4)

firstCInformTable.remove(fourthCGlobalState)
secondCInformTable.remove(eighthCGlobalState)

firstCInformTable.size()
secondCInformTable.size()

firstCInformTable.getObject(0)
secondCInformTable.getObject(0)

firstCInformTable.getInformationTable()
secondCInformTable.getInformationTable()


firstCInformTable.removeIdentObjects()
secondCInformTable.removeIdentObjects()

firstCInformTable.checkIndiscern(1, [1, 2, 3, 4])
secondCInformTable.checkIndiscern(0, [1, 2, 3, 4])

firstCInformTable.copy()
secondCInformTable.copy()

firstCInformTable.printSome()
secondCInformTable.printSome()

firstCInformTable.copyInstance(secondCInformTable)

firstCInformTable.clear()
secondCInformTable.clear()