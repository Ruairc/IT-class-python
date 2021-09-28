#P209 linear searching
#searches within the specific list/array for a specific value
userlist=[85,24,63,45,17,31,96,50,17]
print(userlist.index(17))
#this is one way to do a linear search using an inbuilt method in python
def find_key_in_list(mylist,key):
    for index in range(len(mylist)):
        if mylist[index]==key:
            location=index
            break
    return ("key found at:",location)
"""
this does the same but without the method
for every item in the list it checks if the item is the key
and if it is then it stores it and then breaks
"""      

print(find_key_in_list(userlist,17))