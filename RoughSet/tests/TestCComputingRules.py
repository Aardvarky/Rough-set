import copy
from CImplicant import CImplicant
from CImplArray import CImplArray
from CComputingRules import CComputingRules
from HashableDict import HashableDict
from CGlobalState import CGlobalState
from CInformTable import CInformTable
from CRuleSet import CRuleSet

print("--------------Creating first implicant--------------")

first_implicant = CImplicant(5)
first_implicant.setAll()

print(first_implicant.getBitsetList())

print("--------------Creating second implicant-------------")

second_implicant = CImplicant(5)
second_implicant.setValue(0)
second_implicant.setValue(1)
second_implicant.setValue(2)

print(second_implicant.getBitsetList())

print("--------------Creating third implicant--------------")

third_implicant = CImplicant(5)
third_implicant.setValue(2)
third_implicant.setValue(3)

print(third_implicant.getBitsetList())

print("--------------Creating fourth implicant-------------")

fourth_implicant = CImplicant(5)
fourth_implicant.setValue(2)

print(fourth_implicant.getBitsetList())

print("--------------Creating fifth implicant--------------")

fifth_implicant = CImplicant(5)
fifth_implicant.setAll()

print(first_implicant.getBitsetList())

print("--------------Creating first implicant array--------")

first_implicant_array = CImplArray()
first_implicant_array.append(copy.deepcopy(first_implicant))
first_implicant_array.append(copy.deepcopy(second_implicant))
first_implicant_array.append(copy.deepcopy(third_implicant))
first_implicant_array.append(copy.deepcopy(fourth_implicant))
first_implicant_array.append(copy.deepcopy(fifth_implicant))

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("--------------first hashable dict-------------------------")

fistHashableDict = HashableDict()
fistHashableDict.add(1, 1.0)
fistHashableDict.add(2, 0.0)
fistHashableDict.add(3, 2.0)
fistHashableDict.add(4, 1.0)
fistHashableDict.add(5, 0.0)

print(fistHashableDict)

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

print("--------------first inform table-------------------------")

firstCInformTable = CInformTable()
firstCInformTable.append(firstCGlobalState)
firstCInformTable.append(secondCGlobalState)
firstCInformTable.append(thirdCGlobalState)
firstCInformTable.append(fourthCGlobalState)
firstCInformTable.append(fifthCGlobalState)

print(firstCInformTable.getInformationTable())

print("--------------first CComputing rules---------------------")

firstCComputingRules = CComputingRules()

print("--------------minim Disc Func----------------------------")

second_implicant_array = firstCComputingRules.minimDiscFunc(first_implicant_array)

print(second_implicant_array)

for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("--------------first rule set----------------------------")

firstCRuleSet = CRuleSet()

print(firstCRuleSet.getRuleArray())

print("--------------comp rules--------------------------------")

firstCRuleSet = firstCComputingRules.comRules([1, 2, 3, 4], 5, 5, firstCInformTable, 5)

for i in firstCRuleSet.getRuleArray():
    print("Antecedent : ", i.getAntecedent(),
          " Consequent : ", i.getConsequent(),
          " Support : ", i.getSupport(),
          " Strength : ", i.getStrength(),
          " Coverage : ", i.getCoverage())