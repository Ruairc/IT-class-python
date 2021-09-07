rows=0
cols=0
symbol=input("what symbol do you want to input?:")
rows=int(input("how many rows do you want?:"))
cols=int(input("how many columns do you want?:"))

if rows== int or cols==int:
    for rowindex in range(rows):
        for colindex in range(cols):
            print(symbol,end="")
        print()
else:
    print("invalid input")