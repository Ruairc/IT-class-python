age=int(input("please enter your age:"))
haslearnerslicence=input("do you have doom eternal?(Y/N)")
if age>18 and haslearnerslicence=="Y":
    print("you can apply for your drivers test")
    
elif age<18:
    print("you need to be 17 or older to play doom eternal")


else:
    print("you need to buy the game first")