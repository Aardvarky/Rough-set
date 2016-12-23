from CRule import CRule
from HashableDict import HashableDict

print("--------------first antecedent dict-------------------------")

firstAntecedent = HashableDict()
firstAntecedent.add(1, 1.0)
firstAntecedent.add(2, 2.0)
firstAntecedent.add(3, 3.0)

print(firstAntecedent)

print("--------------second antecedent dict------------------------")

secondAntecedent = HashableDict()
secondAntecedent.add(1, 1.0)
secondAntecedent.add(4, 4.0)

print(secondAntecedent)

print("--------------third antecedent dict-------------------------")

thirdAntecedent = HashableDict()
thirdAntecedent.add(1, 1.0)
thirdAntecedent.add(2, 2.0)

print(thirdAntecedent)

print("--------------fourth antecedent dict------------------------")

fourthAntecedent = HashableDict()
fourthAntecedent.add(3, 3.0)

print(fourthAntecedent)

print("--------------first consequent dict-------------------------")

firstConsequent = HashableDict()
firstConsequent.add(1, 10.0)

print(firstConsequent)

print("--------------second consequent dict------------------------")

secondConsequent = HashableDict()
secondConsequent.add(2, 11.0)

print(secondConsequent)

print("--------------third consequent dict-------------------------")

thirdConsequent = HashableDict()
thirdConsequent.add(3, 12.0)

print(thirdConsequent)

print("--------------fourth consequent dict------------------------")

fourthConsequent = HashableDict()
fourthConsequent.add(4, 13.0)

print("--------------first rule------------------------------------")

firstCRule = CRule()
firstCRule.setAntecedent(firstAntecedent)
firstCRule.setConsequent(firstConsequent)

print(firstCRule)

print("--------------second rule-----------------------------------")

secondCRule = CRule()
secondCRule.setAntecedent(secondAntecedent)
secondCRule.setAntecedent(secondConsequent)

print(secondCRule)

print("--------------third rule------------------------------------")

thirdCRule = CRule()
thirdCRule.setAntecedent(thirdAntecedent)
thirdCRule.setConsequent(thirdConsequent)

print(thirdCRule)

print("--------------fourth rule-----------------------------------")

fourthCRule = CRule()
fourthCRule.setAntecedent(fourthAntecedent)
fourthCRule.setConsequent(fourthConsequent)

print(fourthCRule)

print("--------------get antecedent consequent first rule----------")

print(firstCRule.getAntecedent())
print(firstCRule.getConsequent())

print("--------------get antecedent consequent second rule---------")

print(secondCRule.getAntecedent())
print(secondCRule.getConsequent())

print("--------------get antecedent consequent third rule----------")

print(thirdCRule.getAntecedent())
print(thirdCRule.getConsequent())

print("--------------get antecedent consequent fourth rule---------")

print(fourthCRule.getAntecedent())
print(fourthCRule.getConsequent())

print("--------------set parameter---------------------------------")

firstCRule.setParameter("attribute", "value")
print(firstCRule.getParameter("attribute"))

print("--------------compute cost----------------------------------")

firstCRule.computeCost([1, 2, 3, 4])

print("--------------set and get support---------------------------")

firstCRule.setSupport(2)
print(firstCRule.getSupport())

print("--------------increase support and antsupport---------------")

firstCRule.increaseSupport(1)
firstCRule.increaseAntSupport(1)

print("--------------set and get strength--------------------------")

firstCRule.setStrength(1)
print(firstCRule.getStrength())

print("--------------compute strength------------------------------")

firstCRule.computeStrength(1)

print("--------------set and get coverage--------------------------")

firstCRule.setCoverage(1.0)
print(firstCRule.getCoverage())

print("--------------first Value Of Array--------------------------")

firstValueOfArray = HashableDict()
firstValueOfArray.add(10.0, 1)

print(firstValueOfArray)

print("--------------second Value Of Array-------------------------")

secondValueOfArray = HashableDict()
secondValueOfArray.add(2.0, 0)

print(secondValueOfArray)

print("--------------third Value Of Array--------------------------")

thirdValueOfArray = HashableDict()
thirdValueOfArray.add(3.0, 0)

print(thirdValueOfArray)

print("--------------fourth Value Of Array-------------------------")

fourthValueOfArray = HashableDict()
fourthValueOfArray.add(4.0, 0)

print(fourthValueOfArray)

print("--------------first Values Of Attr--------------------------")

firstValuesOfAttr = HashableDict()
firstValuesOfAttr.add(1, firstValueOfArray)
firstValuesOfAttr.add(2, secondValueOfArray)
firstValuesOfAttr.add(3, thirdValueOfArray)
firstValuesOfAttr.add(4, fourthValueOfArray)

print(firstValuesOfAttr)

print("--------------compute coverage------------------------------")

firstCRule.computeCoverage(firstValuesOfAttr)
print(firstCRule.getCoverage())

print("--------------get certainty---------------------------------")

print(firstCRule.getCertainty())

print("--------------compute certainty-----------------------------")

firstCRule.computeCertainty()
print(firstCRule.getCertainty())

print("--------------compute signature-----------------------------")

firstCRule.computeSignature()

print("--------------check attribute-------------------------------")

print(firstCRule.checkAttribute(0))

print("--------------equal operator--------------------------------")

print(firstCRule.equalOperator(secondCRule))