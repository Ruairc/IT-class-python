while True:
    try:
        num1=int(input("enter the first number:"))
        num2=int(input("enter the second number:"))
    except ValueError:
        print("invalid input")
    else:
        break
if num1>num2:
    print(num1,"is greater than",num2)
elif num1<num2:
    print(num1,"is less than",num2)
else:
    print("they are equal")
