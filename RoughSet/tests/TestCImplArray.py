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
first_implicant_array.append(first_implicant)
first_implicant_array.append(second_implicant)
first_implicant_array.append(third_implicant)
first_implicant_array.append(fourth_implicant)
first_implicant_array.append(fifth_implicant)

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
second_implicant_array.append(sixth_implicant)
second_implicant_array.append(seventh_implicant)
second_implicant_array.append(eighth_implicant)
second_implicant_array.append(ninth_implicant)
second_implicant_array.append(tenth_implicant)

# Sorting
print("-------------------Sorting-------------------")
first_implicant_array.sort()

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

second_implicant_array.sort()
for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("------------------Minimalize-----------------")

# Minimalize
first_implicant_array.minimalize()

for i in first_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

second_implicant_array.minimalize()

for i in second_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("--------------Cartesian operator-------------")

# Cartesian operator
third_implicant_array = first_implicant_array.cartesianOperator(eighth_implicant)

for i in third_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")

fourth_implicant_array = second_implicant_array.cartesianOperator(second_implicant)

for i in fourth_implicant_array.getImplicantArray():
    print(i.getBitsetList())

print("---------------------------------------------")