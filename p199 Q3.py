#Q3
while True:
    try:
        num1=int(input("enter the first number:"))
        num2=int(input("enter the second number:"))
    except ValueError:
        print("invalid input")
    else:
        break
total=num1*num2
print(total)