count=0
mylist=[1,2,3,465,67,432,5,5,7,4,2,4,6,7,5,54,5,5,3,7,43,8]
while True:
    try:
        user_number=int(input("what do number do you need to count?"))
    except ValueError:
        print("Invalid Input")
    else:
        break
for item in mylist:
    if item==user_number:
        count+=1
print(count)
        