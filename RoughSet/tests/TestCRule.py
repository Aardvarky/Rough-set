from CRule import CRule
from HashableDict import HashableDict

firstAntecedent = HashableDict()
firstAntecedent.add(1, 1.0)
firstAntecedent.add(2, 2.0)
firstAntecedent.add(3, 3.0)

secondAntecedent = HashableDict()
secondAntecedent.add(1, 1.0)
secondAntecedent.add(4, 4.0)

thirdAntecedent = HashableDict()
thirdAntecedent.add(1, 1.0)
thirdAntecedent.add(2, 2.0)

fourthAntecedent = HashableDict()
fourthAntecedent.add(3, 3.0)

firstConsequent = HashableDict()
firstConsequent.add(1, 10.0)

secondConsequent = HashableDict()
secondConsequent.add(2, 11.0)

thirdConsequent = HashableDict()
thirdConsequent.add(3, 12.0)

fourthConsequent = HashableDict()
fourthConsequent.add(4, 13.0)

firstCRule = CRule()
firstCRule.setAntecedent(firstAntecedent)
firstCRule.setConsequent(firstConsequent)

secondCRule = CRule()
secondCRule.setAntecedent(secondAntecedent)
secondCRule.setAntecedent(secondConsequent)

thirdCRule = CRule()
thirdCRule.setAntecedent(thirdAntecedent)
thirdCRule.setConsequent(thirdConsequent)

fourthCRule = CRule()
fourthCRule.setAntecedent(fourthAntecedent)
fourthCRule.setConsequent(fourthConsequent)

firstCRule.getAntecedent()
firstCRule.getConsequent()

secondCRule.getAntecedent()
secondCRule.getConsequent()

thirdCRule.getAntecedent()
thirdCRule.getConsequent()

fourthCRule.getAntecedent()
fourthCRule.getConsequent()

firstCRule.setParameter("attribute", "value")

firstCRule.computeCost([1, 2, 3, 4])

firstCRule.getSupport()
firstCRule.setSupport(2)

firstCRule.increaseSupport(1)
firstCRule.increaseAntSupport(1)

firstCRule.getStrength()
firstCRule.setStrength(1)

firstCRule.computeStrength(1)

firstCRule.getCoverage()
firstCRule.setCoverage(1.0)

firstValueOfArray = HashableDict()
firstValueOfArray.add(10.0, 1)

secondValueOfArray = HashableDict()
secondValueOfArray.add(2.0, 0)

thirdValueOfArray = HashableDict()
thirdValueOfArray.add(3.0, 0)

fourthValueOfArray = HashableDict()
fourthValueOfArray.add(4.0, 0)

firstValuesOfAttr = HashableDict()
firstValuesOfAttr.add(1, firstValueOfArray)
firstValuesOfAttr.add(2, secondValueOfArray)
firstValuesOfAttr.add(3, thirdValueOfArray)
firstValuesOfAttr.add(4, fourthValueOfArray)

firstCRule.computeCoverage(firstValuesOfAttr)

firstCRule.getCertainty()

firstCRule.computeCertainty()

firstCRule.computeSignature()

firstCRule.checkAttribute(0)

firstCRule.equalOperator(secondCRule)