import copy
from CImplArray import CImplArray
from CImplicant import CImplicant

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
first_implicant_array.append(copy.deepcopy(first_implicant))
first_implicant_array.append(copy.deepcopy(second_implicant))
first_implicant_array.append(copy.deepcopy(third_implicant))
first_implicant_array.append(copy.deepcopy(fourth_implicant))
first_implicant_array.append(copy.deepcopy(fifth_implicant))

sixth_implicant = CImplicant(4)
sixth_implicant.setValue(0)

seventh_implicant = CImplicant(4)
seventh_implicant.setValue(0)
seventh_implicant.setValue(3)

eighth_implicant = CImplicant(4)
eighth_implicant.setValue(0)
eighth_implicant.setValue(1)
eighth_implicant.setValue(2)

ninth_implicant = CImplicant(4)
ninth_implicant.setAll()

tenth_implicant = CImplicant(4)
tenth_implicant.setValue(0)
tenth_implicant.setValue(1)

second_implicant_array = CImplArray()
second_implicant_array.append(copy.deepcopy(sixth_implicant))
second_implicant_array.append(copy.deepcopy(seventh_implicant))
second_implicant_array.append(copy.deepcopy(eighth_implicant))
second_implicant_array.append(copy.deepcopy(ninth_implicant))
second_implicant_array.append(copy.deepcopy(tenth_implicant))

print("-------------------Sorting-------------------")

first_implicant_array.sort()

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

second_implicant_array.sort()

for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("------------------Minimalize-----------------")

first_implicant_array.minimalize()

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

second_implicant_array.minimalize()

for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("--------------Cartesian operator-------------")

third_implicant_array = first_implicant_array.cartesianOperator(eighth_implicant)

for i in third_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

fourth_implicant_array = second_implicant_array.cartesianOperator(second_implicant)

for i in fourth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------conj2disj---------------------")
print("---------------first conj2disj---------------")

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

fifth_implicant_array = first_implicant_array.conj2disj()

for i in fifth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------second conj2disj--------------")

for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

eighth_implicant_array = second_implicant_array.conj2disj()

for i in eighth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------third conj2disj---------------")

for i in third_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

ninth_implicant_array = third_implicant_array.conj2disj()

for i in ninth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------fourth conj2disj--------------")

for i in fourth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

tenth_implicant_array = fourth_implicant_array.conj2disj()

for i in tenth_implicant_array.getImplicantArray():
    print(i.getBitsetList())