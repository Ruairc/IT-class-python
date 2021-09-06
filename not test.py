#A demo of Python 'not' with 'in' operator
a_List = [5, 10, 15, 20, 25, 30]

for item in a_List:
    if not item in (10,25): 
        print ("List Item: " ,item)
        