inputA=int(input("what temperature is your house actually?"))
inputB=int(input("what temperature do you want your house to be?"))

def thermastatModel(a,b):
    if a>=b:
        return 0
    else:
        return 1
print(thermastatModel(inputA,inputB))