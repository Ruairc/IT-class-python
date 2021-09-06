age=int(input("please enter your age:"))
haslearnerslicence=input("do you have a learners permit?(Y/N)")
if age>17 and haslearnerslicence=="Y":
    print("you can apply for your drivers test")
    
elif age<17:
    print("you need to be 17 or older to apply for a driving test")


else:
    print("you need to get a learners permit first")
