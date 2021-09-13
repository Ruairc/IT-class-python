#functions are mini programmes that run in our code
#print and input are functions that run in our code
#to make a function you must first define it
#once your code is defined you can simply call it by using the name of the function followed by brackets
#we use functions for efficancy and to stop us rewriting code
def menu():
    print("\t***************")
    print("\t*    menu     *")
    print("\t***************")
def menuopt(a):
    print("\t***************")
    print("\t*   option ",a,"*")
    print("\t***************")

#the while statement is just for error correction and stops when
#the correct number is inputted the variable error_correction stops
#being 1 and the while loop stops
error_correction=1

while error_correction==1:
    while True:
        try:
            menu()
            choice=int(input("enter your option:"))
        except ValueError:
            print("try again")
        else:
            break
        
    if choice==1:
        menuopt(1)
        error_correction=0
    elif choice==2:
        menuopt(2)
        error_correction=0
    else:
        print("invalid input")
