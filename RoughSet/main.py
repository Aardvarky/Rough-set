from Bitset import Bitset
from CImplicant import CImplicant
from CDiscernMatrix import CDiscernMatrix
from CGlobalState import CGlobalState

bitset = Bitset(4)

bitset.append(0) # Add bit at left side
bitset.appendString("1") # Add string representation of bit value at left side
bitset.setValue(1) # set 1 or logic true in given index
bitset.setValueAtIndex(0, 1) # set value in given index
bitset.setAll() # set all bits on logic true value

bitset.remove(0) # remove bit from sequence
print(bitset.pop(0)) # return removed element form bitset

print(bitset.count(1)) # counting specific given value

bitset.reverse() # reverse order
bitset.reset() # setting all value at 0
bitset.resetBinaryValue(0) # reset value at given index
bitset.size() # return size of bitset
bitset.test(0) # if value is equal 0 return false otherwise return true
bitset.any() # if any one bit is 1 return true otherwise false
bitset.none() # if none bit is 1 return true
bitset.all() # if all bit are 1 return true
bitset.getBitsetList() # return list of bits
bitset.getElement(0) # return element
bitset.toString() # convert bitset to string representation
bitset.toInt() # convert to decimal value


implicant = CImplicant(4)
implicant.setValue(0)
implicant.setValue(2)
implicant2 = CImplicant(4)
implicant2.setValue(1)
implicant2.setValue(3)

implicant3 = CImplicant(4)
implicant3.copyInstance(implicant)
print(implicant3.getBitsetList())

implicant.orOperator(implicant2)
print(implicant.getBitsetList())

implicant.reset()
implicant.assignOperator(implicant2)
print(implicant.getBitsetList())

print(implicant.inclusionOperator(implicant3))

state = CGlobalState()
state.setName("global state 1")
state.setDescriptors({1: 2.3, 2: 2.4})

state1 = CGlobalState()
state1.setName("global state 2")
state1.setDescriptors({1: 2.3, 2: 2.4})

state2 = CGlobalState()

state2.addDescriptor(3, 2.2)
print(state2.getDescriptors())

state2.copyInstance(state)
print(state2.getDescriptors())

print(state.getAttributeValue(1))
print(state.getDescriptors())
state.setDescriptors(state2.getDescriptors())
print(state.getDescriptors())

# discernMatrix = CDiscernMatrix(4)

# for row in discernMatrix.getTab():
#     for cell in row:
#         cell.append(1)
#
# for row in discernMatrix.getTab():
#     for cell in row:
#         print(repr(cell.getBitsetList()).rjust(3), end=' ')
#     print()