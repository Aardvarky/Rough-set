from Bitset import Bitset

secondBitset = Bitset(6)
secondBitset.setAll()

firstBitset = Bitset(6)

firstBitset.append(0)
firstBitset.append(1)

firstBitset.appendString("0")
firstBitset.appendString("1")

firstBitset.setValue(0)

firstBitset.setValueAtIndex(1, 0)

firstBitset.setAll()

firstBitset.remove(0)

firstBitset.pop(0)

firstBitset.count(0)
firstBitset.count(1)

firstBitset.reverse()

firstBitset.resetBinaryValue(0)

firstBitset.reset()

firstBitset.size()

firstBitset.test(0)
firstBitset.test(1)

firstBitset.any()

firstBitset.none()

firstBitset.all()

firstBitset.getBitsetList()

firstBitset.getElement(0)

firstBitset.toString()

firstBitset.toInt()

firstBitset.flip()

firstBitset.orOperat(secondBitset)