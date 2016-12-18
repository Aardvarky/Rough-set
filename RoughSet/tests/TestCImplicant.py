from CImplicant import CImplicant

secondImplicant = CImplicant(6)
secondImplicant.setAll()

firstImplicant = CImplicant(6)

firstImplicant.append(0)
firstImplicant.append(1)

firstImplicant.appendString("0")
firstImplicant.appendString("1")

firstImplicant.setValue(0)

firstImplicant.setValueAtIndex(1, 0)

firstImplicant.setAll()

firstImplicant.remove(0)

firstImplicant.pop(0)

firstImplicant.count(0)
firstImplicant.count(1)

firstImplicant.reverse()

firstImplicant.resetBinaryValue(0)

firstImplicant.reset()

firstImplicant.size()

firstImplicant.test(0)
firstImplicant.test(1)

firstImplicant.any()

firstImplicant.none()

firstImplicant.all()

firstImplicant.getBitsetList()

firstImplicant.getElement(0)

firstImplicant.toString()

firstImplicant.toInt()

firstImplicant.flip()

firstImplicant.orOperator(secondImplicant)

firstImplicant.andOperator(secondImplicant)

firstImplicant.assignOperator(secondImplicant)

firstImplicant.inclusionOperator(secondImplicant)