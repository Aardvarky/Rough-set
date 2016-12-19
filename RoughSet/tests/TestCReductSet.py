from CReduct import CReduct
from CReductSet import CReductSet
from CImplicant import CImplicant
from CImplArray import CImplArray

first_implicant = CImplicant(4)
first_implicant.setAll()

second_implicant = CImplicant(4)
second_implicant.setValue(0)
second_implicant.setValue(1)
second_implicant.setValue(2)

third_implicant = CImplicant(4)
third_implicant.setValue(2)
third_implicant.setValue(3)

fourth_implicant = CImplicant(4)
fourth_implicant.setValue(2)

fifth_implicant = CImplicant(4)
fifth_implicant.reset()

first_implicant_array = CImplArray()
first_implicant_array.append(first_implicant)
first_implicant_array.append(second_implicant)
first_implicant_array.append(third_implicant)
first_implicant_array.append(fourth_implicant)
first_implicant_array.append(fifth_implicant)

firstCReduct = CReduct(4)
firstCReduct.setName(1)
firstCReduct.setChoice(False)

secondCReduct = CReduct(4)
secondCReduct.setName(2)
secondCReduct.setChoice(True)

thridCReduct = CReduct(4)
thridCReduct.setName(3)
thridCReduct.setChoice(False)

fourthCReduct = CReduct(4)
fourthCReduct.setName(4)
fourthCReduct.setChoice(True)

firstCReductSet = CReductSet()
firstCReductSet.append(firstCReduct)
firstCReductSet.append(secondCReduct)
firstCReductSet.append(thridCReduct)

firstCReductSet.insert(3, fourthCReduct)

firstCReductSet.getReduct(0)

firstCReductSet.write(first_implicant_array, 4)

firstCReductSet.getReducts()
