import statistics

mylist=[1,3,6,5,7,8,7,10]

mylist.sort()
if len(mylist)%2==0:
    middleplusone=len(mylist)//2
    median=(mylist[middleplusone-1] + mylist[middleplusone])/2
    
else:
    middle=len(mylist)//2
    median=mylist[middle]
    
print("The median is:", median)