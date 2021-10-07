mylist=[85,24,63,45,17,31,96,50]
for index in range(len(mylist)-1):
    print(mylist)
    nextMinValue=min(mylist[index+1:])
    if nextMinValue< mylist[index]:
        nextMinIndex=mylist.index(nextMinValue)
        mylist[nextMinIndex]=mylist[index]
        mylist[index]=nextMinValue
print(mylist)