#Q4
total=0
while True:
    try:
        base_num=int(input("enter the first number:"))
        index_num=int(input("enter the second number:"))
    except ValueError:
        print("invalid input")
    else:
        break
#index_num=index_num+1
total+=base_num
for i in range(1,index_num): 
    total=total*base_num
print("your total is",total)