age=int(input("how old is your computer (in years only min 1):"))
cputype=input("whats your cpu brand intel or amd?(a/i)")
if age>=8 or cputype=="i":
    print("your pc is bad and you should feel bad")
else:
    print("your pc should be ok")