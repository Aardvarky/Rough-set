import copy
from CReduct import CReduct
from CReductSet import CReductSet
from CImplicant import CImplicant
from CImplArray import CImplArray

print("--------------Creating first implicant--------------")

first_implicant = CImplicant(4)
first_implicant.setAll()

print(first_implicant.getBitsetList())

print("--------------Creating seocnd implicant-------------")

second_implicant = CImplicant(4)
second_implicant.setValue(0)
second_implicant.setValue(1)
second_implicant.setValue(2)

print(second_implicant.getBitsetList())

print("--------------Creating third implicant--------------")

third_implicant = CImplicant(4)
third_implicant.setValue(2)
third_implicant.setValue(3)

print(third_implicant.getBitsetList())

print("--------------Creating fourth implicant-------------")

fourth_implicant = CImplicant(4)
fourth_implicant.setValue(2)

print(fourth_implicant.getBitsetList())

print("--------------Creating fifth implicant--------------")

fifth_implicant = CImplicant(4)
fifth_implicant.reset()

print(fifth_implicant.getBitsetList())

print("--------------first implicant array-----------------")

first_implicant_array = CImplArray()
first_implicant_array.append(first_implicant)
first_implicant_array.append(second_implicant)
first_implicant_array.append(third_implicant)
first_implicant_array.append(fourth_implicant)
first_implicant_array.append(fifth_implicant)

print(first_implicant_array.getImplicantArray())

print("--------------first reduct--------------------------")

firstCReduct = CReduct(4)
firstCReduct.setName(1)
firstCReduct.setChoice(False)

print(firstCReduct)

print("--------------second reduct-------------------------")

secondCReduct = CReduct(4)
secondCReduct.setName(2)
secondCReduct.setChoice(True)

print(secondCReduct)

print("--------------third reduct--------------------------")

thirdCReduct = CReduct(4)
thirdCReduct.setName(3)
thirdCReduct.setChoice(False)

print(thirdCReduct)

print("--------------fourth reduct-------------------------")

fourthCReduct = CReduct(4)
fourthCReduct.setName(4)
fourthCReduct.setChoice(True)

print(fourthCReduct)

print("--------------first reduct set----------------------")

firstCReductSet = CReductSet()
firstCReductSet.append(firstCReduct)
firstCReductSet.append(secondCReduct)
firstCReductSet.append(thirdCReduct)

print(firstCReductSet.getReducts())

print("--------------insert reduct set---------------------")

firstCReductSet.insert(3, fourthCReduct)

print(firstCReductSet.getReducts())

print("--------------get reduct set------------------------")

print(firstCReductSet.getReduct(0))

print("--------------write reduct set----------------------")

firstCReductSet.write(copy.deepcopy(first_implicant_array), 4)

print(firstCReductSet.getReducts())

print("--------------get reducts reduct set----------------")

print(firstCReductSet.getReducts())