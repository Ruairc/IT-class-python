rain=[]
total=0
for i in range(7):
    cm=float(input("how much rain fell today?"))
    rain.append(cm)
for item in (rain):
    total+=item
print("the total amount of rain that fell this week is:",total,"cm")
print("the average is",total/7,"cm")
for item in (rain):
    if item>=3.5:
        print("rain exceeded 3.5 on the day that",item,"cm of rain fell")
