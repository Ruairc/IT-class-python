rows=0 

cols=0 



rows=int(input("how many rows do you want?:")) 
cols=int(input("how many columns do you want?:")) 
symbol=input("what symbol do you want to input?:")  


while rows>=2000 or cols>=2000:
    print("that number is too high")
    rows=int(input("how many rows do you want?:")) 
    cols=int(input("how many columns do you want?:")) 


for rowindex in range(rows): 
    for colindex in range(cols):
        print(symbol,end="") 
    print()
