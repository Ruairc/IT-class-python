#P213 Q4
mylist=[19,87,1,-1,11,0,-1,33,19]
key1=-1
key2=33
key3=117
location=0
def linear_search(key,a):
    for index in range(len(mylist)):
        if mylist[index]==key:
            location=index
            break
        else:
            location=-1
    print("key ",a,"found at:",location)
linear_search(key1,1)
linear_search(key2,2)
linear_search(key3,3)
