mylist=[85,24,63,45,17,31,96,50]
key=17
for index in range(len(mylist)):
    if mylist[index]==key:
        location=index
print("key found at:",location)