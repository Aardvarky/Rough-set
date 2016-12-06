from CRule import CRule
from HashableDict import HashableDict
from random import randint
from CRuleSet import CRuleSet

consequent = HashableDict()
consequent.add(randint(0, 100), 1.0)
consequent.add(randint(0, 100), 2.0)
consequent.add(randint(0, 100), 3.0)
consequent.add(randint(0, 100), 4.0)

consequent1 = HashableDict()
consequent1.add(100, 1.0)
consequent1.add(200, 2.0)
consequent1.add(300, 3.0)
consequent1.add(400, 4.0)

consequent2 = HashableDict()
consequent2.add(100, 1.0)
consequent2.add(200, 2.0)
consequent2.add(300, 3.0)
consequent2.add(400, 4.0)

consequent3 = HashableDict()
consequent3.add(400, 1.0)
consequent3.add(500, 2.0)
consequent3.add(600, 3.0)
consequent3.add(700, 4.0)

consequent4 = HashableDict()
consequent4.add(400, 1.0)
consequent4.add(500, 2.0)
consequent4.add(600, 3.0)
consequent4.add(700, 4.0)

antecedent = HashableDict()
antecedent.add(randint(0, 100), 1.0)
antecedent.add(randint(0, 100), 2.0)
antecedent.add(randint(0, 100), 3.0)
antecedent.add(randint(0, 100), 4.0)

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

print(cRuleSet.getRuleArray())
cRuleSet.removeRules(1)
print(cRuleSet.getRuleArray())