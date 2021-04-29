import statistics
num=0
mean=0
reps=int(input("how many numbers do you want to average?: "))

for i in range(reps):
    num=int(input("enter a number:"))
    mean=num+mean
mean=mean/reps
print("your mean is %.2f:", mean)
    
