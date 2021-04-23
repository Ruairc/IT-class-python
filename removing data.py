numList=[3,5,-7,56,-27,53,-69]
print("look at all the numbers", numList)

for item in numList:
    if item <0:
        numList.remove(item)
print(numList)