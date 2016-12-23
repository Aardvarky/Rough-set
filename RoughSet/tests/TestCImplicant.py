from CImplicant import CImplicant

print("--------------Creating second implicant-------------")

secondImplicant = CImplicant(6)
secondImplicant.setAll()

print(secondImplicant.getBitsetList())

print("--------------Creating first implicant--------------")

firstImplicant = CImplicant(6)

print(firstImplicant.getBitsetList())

print("--------------append method----------------------")

firstImplicant.append(0)
firstImplicant.append(1)

print(firstImplicant.getBitsetList())

print("--------------append string method---------------")

firstImplicant.appendString("0")
firstImplicant.appendString("1")

print(firstImplicant.getBitsetList())

print("--------------set value method-------------------")

firstImplicant.setValue(0)

print(firstImplicant.getBitsetList())

print("--------------set value at index method----------")

firstImplicant.setValueAtIndex(1, 1)

print(firstImplicant.getBitsetList())

print("--------------set all method---------------------")

firstImplicant.setAll()

print(firstImplicant.getBitsetList())

print("--------------remove method----------------------")

firstImplicant.remove(0)

print(firstImplicant.getBitsetList())

print("--------------pop method-------------------------")

print(firstImplicant.pop(0))

print(firstImplicant.getBitsetList())

print("--------------count method-----------------------")

print(firstImplicant.count(0))
print(firstImplicant.count(1))

print("--------------reverse method---------------------")

firstImplicant.reverse()

print(firstImplicant.getBitsetList())

print("--------------reset binary value method----------")

firstImplicant.resetBinaryValue(0)

print(firstImplicant.getBitsetList())

print("--------------reset method-----------------------")

firstImplicant.reset()

print(firstImplicant.getBitsetList())

print("--------------size method------------------------")

print(firstImplicant.size())

print("--------------test method------------------------")

print(firstImplicant.test(0))
print(firstImplicant.test(1))

print("--------------any method-------------------------")

print(firstImplicant.any())

print("--------------none method------------------------")

print(firstImplicant.none())

print("--------------all method-------------------------")

print(firstImplicant.all())

print("--------------get bitset list method--------------")

print(firstImplicant.getBitsetList())

print("--------------get element method------------------")

print(firstImplicant.getElement(0))

print("--------------to string method--------------------")

print(firstImplicant.toString())

print("--------------to int method-----------------------")

print(firstImplicant.toInt())

print("--------------flip method-------------------------")

firstImplicant.flip()

print(firstImplicant.getBitsetList())

print("--------------or operator method------------------")

firstImplicant.orOperator(secondImplicant)

print(firstImplicant.getBitsetList())
print(secondImplicant.getBitsetList())

print("--------------and operator method-----------------")

thirdImplicant = firstImplicant.andOperator(secondImplicant)

print(thirdImplicant.getBitsetList())

print("--------------assign operator method--------------")

firstImplicant.assignOperator(secondImplicant)

print(firstImplicant.getBitsetList())

print("--------------incusion operator method------------------")

print(firstImplicant.inclusionOperator(secondImplicant))