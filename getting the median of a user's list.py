import statistics
data=0
userlist=[]

size=int(input("how big do you want your list to be?: "))

for i in range(size):
    data=int(input("enter a number: "))
    userlist.append(data)
    


userlist.sort()

if len(userlist)%2==0:
    middleplusone=len(userlist)//2
    median=(userlist[middleplusone-1] + userlist[middleplusone])/2
    
else:
    middle=len(userlist)//2
    median=userlist[middle]
    
print("The median is:", median)
