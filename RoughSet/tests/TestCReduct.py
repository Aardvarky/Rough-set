from CReduct import CReduct


print("--------------Creating first reduct-------------")

firstCReduct = CReduct(4)

print(firstCReduct.getAttributes().getBitsetList())

print("--------------Creating second reduct------------")
secondCReduct = CReduct(4)

print(secondCReduct.getAttributes().getBitsetList())

print("--------------get and set choice----------------")

firstCReduct.setChoice(False)
print(firstCReduct.getChoice())

print("--------------is chosen-------------------------")

print(firstCReduct.isChosen())

print("--------------set and get-----------------------")

firstCReduct.setName(1)
print(firstCReduct.getName())

print("--------------get attributes--------------------")

print(firstCReduct.getAttributes().getBitsetList())

print("--------------get attributes to int-------------")

print(firstCReduct.getAttributesAsInt())