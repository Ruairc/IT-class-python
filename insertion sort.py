mylist=[85,24,63,45,17,31,96,50]
for index in range(1,len(mylist)):
    print(mylist)
    itemInsert=mylist[index]
    position=index
    while position>0 and mylist[position-1]>itemInsert:
        mylist[position]=mylist[position-1]
        position-=1
    mylist[position]=itemInsert
print(mylist)
