from CInformTable import CInformTable
from HashableDict import HashableDict
from CGlobalState import CGlobalState
from BasicInformSystem import BasicInformSystem
from BasicInformSystem2 import BasicInformSystem2

print("--------------first hashable dict-------------------------")

fistHashableDict = HashableDict()
fistHashableDict.add(1, 1.0)
fistHashableDict.add(2, 0.0)
fistHashableDict.add(3, 2.0)
fistHashableDict.add(4, 1.0)
fistHashableDict.add(5, 0.0)

print(fistHashableDict)

print("--------------first global state-------------------------")

firstCGlobalState = CGlobalState()
firstCGlobalState.setName("G1")
firstCGlobalState.setDescriptors(fistHashableDict)

print(firstCGlobalState)

print("--------------Creating first hashable dict--------------------")

firstValueOfAttrHashableDict = HashableDict()
firstValueOfAttrHashableDict.add(1.0, 1)

print(firstValueOfAttrHashableDict)

print("--------------Creating first hashable dict--------------------")

firstValueOfAttrDict = HashableDict()
firstValueOfAttrDict.add(1, firstValueOfAttrHashableDict)

print(firstValueOfAttrDict)

print("--------------second hashable dict------------------------")

secondHashableDict = HashableDict()
secondHashableDict.add(1, 0.0)
secondHashableDict.add(2, 0.0)
secondHashableDict.add(3, 1.0)
secondHashableDict.add(4, 2.0)
secondHashableDict.add(5, 1.0)

print(secondHashableDict)

print("--------------third hashable dict------------------------")

thirdHashableDict = HashableDict()
thirdHashableDict.add(1, 2.0)
thirdHashableDict.add(2, 0.0)
thirdHashableDict.add(3, 2.0)
thirdHashableDict.add(4, 1.0)
thirdHashableDict.add(5, 0.0)

print(thirdHashableDict)

print("--------------fourth hashable dict-----------------------")

fourthHashableDict = HashableDict()
fourthHashableDict.add(1, 0.0)
fourthHashableDict.add(2, 0.0)
fourthHashableDict.add(3, 2.0)
fourthHashableDict.add(4, 2.0)
fourthHashableDict.add(5, 2.0)

print(fourthHashableDict)

print("--------------fourth hashable dict-----------------------")

fifthHashableDict = HashableDict()
fifthHashableDict.add(1, 1.0)
fifthHashableDict.add(2, 1.0)
fifthHashableDict.add(3, 2.0)
fifthHashableDict.add(4, 1.0)
fifthHashableDict.add(5, 0.0)

print(fifthHashableDict)

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

print("--------------first inform table-------------------------")

firstCInformTable = CInformTable()
firstCInformTable.append(secondCGlobalState)
firstCInformTable.append(thirdCGlobalState)
firstCInformTable.append(fourthCGlobalState)
firstCInformTable.append(fifthCGlobalState)

print(firstCInformTable.getInformationTable())

print("--------------Creating first Basic inform system--------------")

firstBasicInformSystem = BasicInformSystem2(5)

print("--------------set and get name--------------------------------")

firstBasicInformSystem.setName("First Basic Inform System")
print(firstBasicInformSystem.getName())

print("--------------set and get system type-------------------------")

firstBasicInformSystem.setSystemType("Basic inform system")
print(firstBasicInformSystem.getSystemType())

print("--------------get and set attributes--------------------------")

firstBasicInformSystem.setAttributes(1)
print(firstBasicInformSystem.getAttributes().getBitsetList())

print("--------------get and set attribute numbers-------------------")

firstBasicInformSystem.setAttributeNumber(5)
print(firstBasicInformSystem.getAttributeNumber())

print("--------------get and set attribute names/name----------------")

firstBasicInformSystem.setAttributeNames(["a", "b", "c", "d", "e"])
print(firstBasicInformSystem.getAttributeNames())
print(firstBasicInformSystem.getAttributeName(0))

print("--------------get and set attribute indexes-------------------")

firstBasicInformSystem.setAttributeIndexes(HashableDict({"index1": 1}))
print(firstBasicInformSystem.getAttributeIndexes())

print("--------------get and set attribute types---------------------")

firstBasicInformSystem.setAttributeTypes([float, float, float, float, float])
print(firstBasicInformSystem.getAttributeTypes())
print(firstBasicInformSystem.getAttributeType(0))

print("--------------get and set attribute costs---------------------")

firstBasicInformSystem.setAttributeCosts([1.0, 0.0, 1.0, 1.0, 1.0])
print(firstBasicInformSystem.getAttributeCosts())

print("--------------get and set attribute values--------------------")

firstBasicInformSystem.setAttributeValues(firstValueOfAttrDict)
print(firstBasicInformSystem.getAttributeValues())

print("--------------get and set object------------------------------")

firstBasicInformSystem.setObject(0, firstCGlobalState)
print(firstBasicInformSystem.getObject(0).getDescriptors())

print("--------------get and set object name-------------------------")

firstBasicInformSystem.setObjectName(0, "name")
print(firstBasicInformSystem.getObjectName(0))

print("--------------get and set objects-----------------------------")

firstBasicInformSystem.setObjects(firstCInformTable)

for i in firstBasicInformSystem.getObjects().getInformationTable():
    print(i.getDescriptors())

print("--------------get and set object number-----------------------")

firstBasicInformSystem.setObjectNumber(4)
print(firstBasicInformSystem.getObjectNumber())

print("--------------get object CDiscern matrix----------------------")

print(firstBasicInformSystem.getDiscernMatrix())

print("--------------compute reducts---------------------------------")

firstBasicInformSystem.computeReducts()

for i in firstBasicInformSystem.getReducts().getReducts():
    print("Reduct name : ", i.getName(),
          " Reduct choise : ", i.getChoice(),
          " Reduct attributes : ", i.getAttributes().getBitsetList())

print("--------------compute reducts using indexes-------------------")

firstBasicInformSystem.computeReductsUsingAttributes(1, 3)

for i in firstBasicInformSystem.getReducts().getReducts():
    print("Reduct name : ", i.getName(),
          " Reduct choise : ", i.getChoice(),
          " Reduct attributes : ", i.getAttributes().getBitsetList())