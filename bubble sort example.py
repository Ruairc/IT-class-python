mylist=[85,24,63,45,17,31,96,50]
for outerIndex in range(len(mylist)-1):
    print(mylist)
    for index in range (len(mylist)-1):
        if mylist[index]>mylist[index+1]:
            tempValue=mylist[index]
            mylist[index]=mylist[index+1]
            mylist[index+1]=tempValue
print(mylist)
            