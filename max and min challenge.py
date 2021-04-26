min=0
max=0
currentmax=0
currentmin=9999999999999999999999999999999999999999999999999
        
file = open("mynewcsv.csv", "w")
file.write("33,44,777,88,22")
file.close()
file = open("mynewcsv.csv", "r")
mylist= file.read()

mylist=[int(item) for item in mylist]
for item in mylist:
    if item > currentmax:
        currentmax=item
max=currentmax
print(max)
    



for item in mylist:
    if item < currentmin:
        currentmin=item
min=currentmin
print(min)