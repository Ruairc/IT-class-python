symbol=input("what symbol do you want to input?:") 
rows=int(input("how many rows do you want?:"))  
#this bit gathers inputs

rows+=1
#the line below stops people from entering high numbers
while rows>500 or rows<1:
    print("That number is too high(or a negative)")
    rows=int(input("how many rows do you want?:")) 

#this is basically 2 nested for loops the first loop starts at 1 and ends at the user's chosen number+1
#the loop iterations start with the number 0 
for i in range(1,rows):
    print(" ")
    for j in range(i):
        print(symbol,end="") 
    print()
