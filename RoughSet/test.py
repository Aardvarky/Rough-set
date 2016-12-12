from CRule import CRule
from HashableDict import HashableDict
from CRuleSet import CRuleSet
from BasicInformSystem import BasicInformSystem
import random

consequent = HashableDict()
consequent.add(1, 1.0)
consequent.add(2, 2.0)
consequent.add(3, 3.0)
consequent.add(4, 4.0)

consequent1 = HashableDict()
consequent1.add(1, 1.0)
consequent1.add(2, 2.0)
consequent1.add(3, 3.0)
consequent1.add(4, 4.0)

consequent2 = HashableDict()
consequent2.add(1, 1.0)
consequent2.add(2, 2.0)
consequent2.add(3, 3.0)
consequent2.add(4, 4.0)

consequent3 = HashableDict()
consequent3.add(4, 4.0)
consequent3.add(5, 5.0)
consequent3.add(6, 6.0)
consequent3.add(7, 7.0)

consequent4 = HashableDict()
consequent4.add(4, 4.0)
consequent4.add(5, 5.0)
consequent4.add(6, 6.0)
consequent4.add(7, 7.0)

antecedent = HashableDict()
antecedent.add(10, 1.0)
antecedent.add(20, 2.0)
antecedent.add(30, 3.0)
antecedent.add(40, 4.0)

antecedent1 = HashableDict()
antecedent1.add(10, 1.0)
antecedent1.add(20, 2.0)
antecedent1.add(30, 3.0)
antecedent1.add(40, 4.0)

antecedent2 = HashableDict()
antecedent2.add(10, 1.0)
antecedent2.add(20, 2.0)
antecedent2.add(30, 3.0)
antecedent2.add(40, 4.0)

antecedent3 = HashableDict()
antecedent3.add(50, 1.0)
antecedent3.add(60, 2.0)
antecedent3.add(70, 3.0)
antecedent3.add(80, 4.0)

antecedent4 = HashableDict()
antecedent4.add(50, 1.0)
antecedent4.add(60, 2.0)
antecedent4.add(70, 3.0)
antecedent4.add(80, 4.0)

cRule = CRule()
cRule.setConsequent(consequent)
cRule.setAntecedent(antecedent)

cRule1 = CRule()
cRule1.setConsequent(consequent1)
cRule1.setAntecedent(antecedent1)

cRule2 = CRule()
cRule2.setConsequent(consequent2)
cRule2.setAntecedent(antecedent2)

cRule3 = CRule()
cRule3.setConsequent(consequent3)
cRule3.setAntecedent(antecedent3)

cRule4 = CRule()
cRule4.setConsequent(consequent4)
cRule4.setAntecedent(antecedent4)

cRuleSet = CRuleSet()
cRuleSet.append(cRule)
cRuleSet.append(cRule1)
cRuleSet.append(cRule2)
cRuleSet.append(cRule3)
cRuleSet.append(cRule4)

cRuleSet1 = CRuleSet()

DictForParameter = dict()
DictForParameter[1.0] = 1
DictForParameter[2.0] = 1
DictForParameter[3.0] = 1
DictForParameter[4.0] = 1

dictyes = dict()
dictyes[1] = DictForParameter
dictyes[2] = DictForParameter
dictyes[3] = DictForParameter
dictyes[4] = DictForParameter
dictyes[5] = DictForParameter


cRuleSet1 = cRuleSet.compInhibRules(dictyes, cRuleSet1)

basicInformSystem = BasicInformSystem()
basicInformSystem.setObjectNumber(2)
basicInformSystem.setAttributeNumber(2)
basicInformSystem.compDiscernMatrix()