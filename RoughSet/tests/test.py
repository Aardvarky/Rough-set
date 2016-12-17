from HashableDict import HashableDict
from CGlobalState import CGlobalState
from BasicInformSystem import BasicInformSystem
from CInformTable import CInformTable
from CImplicant import CImplicant
from CImplArray import CImplArray

indexesAttributeMap = HashableDict()
indexesAttributeMap.add("firstProduct", 0)
indexesAttributeMap.add("secondProduct", 1)
indexesAttributeMap.add("thirdProduct", 2)
indexesAttributeMap.add("fourthProduct", 3)

firstGlobalDict = HashableDict()
firstGlobalDict.add(0, 1.0)
firstGlobalDict.add(1, 2.0)
firstGlobalDict.add(2, 0.0)
firstGlobalDict.add(3, 0.0)

secondGlobalDict = HashableDict()
secondGlobalDict.add(0, 6.0)
secondGlobalDict.add(1, 3.0)
secondGlobalDict.add(2, 1.0)
secondGlobalDict.add(3, 4.0)

thirdGlobalDict = HashableDict()
thirdGlobalDict.add(0, 6.0)
thirdGlobalDict.add(1, 5.0)
thirdGlobalDict.add(2, 3.0)
thirdGlobalDict.add(3, 2.0)

fourthGlobalDict = HashableDict()
fourthGlobalDict.add(0, 6.0)
fourthGlobalDict.add(1, 1.0)
fourthGlobalDict.add(2, 3.0)
fourthGlobalDict.add(3, 2.0)

fifthGlobalDict = HashableDict()
fifthGlobalDict.add(0, 5.0)
fifthGlobalDict.add(1, 1.0)
fifthGlobalDict.add(2, 3.0)
fifthGlobalDict.add(3, 2.0)

firstGlobalState = CGlobalState()
firstGlobalState.setName("first")
firstGlobalState.setDescriptors(firstGlobalDict)

secondGlobalState = CGlobalState()
secondGlobalState.setName("second")
secondGlobalState.setDescriptors(secondGlobalDict)

thirdGlobalState = CGlobalState()
thirdGlobalState.setName("third")
thirdGlobalState.setDescriptors(thirdGlobalDict)

fourthGlobalState = CGlobalState()
fourthGlobalState.setName("fourth")
fourthGlobalState.setDescriptors(fourthGlobalDict)

fifthGlobalState = CGlobalState()
fifthGlobalState.setName("fifth")
fifthGlobalState.setDescriptors(fifthGlobalDict)

informTable = CInformTable()
informTable.append(firstGlobalState)
informTable.append(secondGlobalState)
informTable.append(thirdGlobalState)
informTable.append(fourthGlobalState)
informTable.append(fifthGlobalState)

basicInformSystem = BasicInformSystem()
basicInformSystem.setName("Basic info system")
basicInformSystem.setSystemType("Normal type")
basicInformSystem.setAttributeNumber(4)
basicInformSystem.setAttributeNames(["firstProduct",
                                     "secondProduct",
                                     "thirdProduct",
                                     "fourthProduct"])

basicInformSystem.setAttributeIndexes(indexesAttributeMap)
basicInformSystem.setInformTable(informTable)
basicInformSystem.compDiscernMatrix()
basicInformSystem.compNondetRules([0, 1, 2, 3], 3)
basicInformSystem.compDependDegreeForAttribute([0, 1, 2, 3], 3)
basicInformSystem.compDependDegreeForAttributes([0, 1, 2, 3], [0, 1, 2, 3])

cImplicant = CImplicant(4)
cImplArray = CImplArray()
cImplArray.append(cImplicant)
cImplArray.append(cImplicant)
cImplArray.append(cImplicant)
cImplArray.append(cImplicant)
cImplArray.sort()