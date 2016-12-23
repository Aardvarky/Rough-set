from Bitset import Bitset

print("--------------Creating second bitset-------------")
secondBitset = Bitset(6)
secondBitset.setAll()

print(secondBitset.getBitsetList())

print("--------------Creating first bitset--------------")

firstBitset = Bitset(6)
print(firstBitset.getBitsetList())

print("--------------append method----------------------")

firstBitset.append(0)
firstBitset.append(1)

print(firstBitset.getBitsetList())

print("--------------append string method---------------")

firstBitset.appendString("0")
firstBitset.appendString("1")

print(firstBitset.getBitsetList())

print("--------------set value method-------------------")

firstBitset.setValue(0)

print(firstBitset.getBitsetList())

print("--------------set value at index method----------")

firstBitset.setValueAtIndex(1, 1)

print(firstBitset.getBitsetList())

print("--------------set all method---------------------")

firstBitset.setAll()
print(firstBitset.getBitsetList())

print("--------------remove method----------------------")

firstBitset.remove(0)

print(firstBitset.getBitsetList())

print("--------------pop method-------------------------")

print(firstBitset.pop(0))

print(firstBitset.getBitsetList())

print("--------------count method-----------------------")

print(firstBitset.count(0))
print(firstBitset.count(1))

print("--------------reverse method---------------------")

firstBitset.reverse()

print(firstBitset.getBitsetList())

print("--------------reset binary value method----------")

firstBitset.resetBinaryValue(0)

print(firstBitset.getBitsetList())

print("--------------reset method-----------------------")

firstBitset.reset()

print(firstBitset.getBitsetList())

print("--------------size method------------------------")

print(firstBitset.size())

print("--------------test method------------------------")

print(firstBitset.test(0))
print(firstBitset.test(1))

print("--------------any method-------------------------")

print(firstBitset.any())

print("--------------none method------------------------")

print(firstBitset.none())

print("--------------all method-------------------------")

print(firstBitset.all())

print("--------------get bitset list method--------------")

print(firstBitset.getBitsetList())

print("--------------get element method------------------")

print(firstBitset.getElement(0))

print("--------------to string method--------------------")

print(firstBitset.toString())

print("--------------to int method-----------------------")

print(firstBitset.toInt())

print("--------------flip method-------------------------")

firstBitset.flip()

print(firstBitset.getBitsetList())

print("--------------or operator method------------------")

firstBitset.orOperat(secondBitset)

print(secondBitset.getBitsetList())
print(firstBitset.getBitsetList())