myList[1,3,6,-23,-2,-58]
print("Original list", myList)

index= 0

for item in myList:
    if myList[index]<0:
        myList[index]="no neg values here"
    index +=1
print(myList)