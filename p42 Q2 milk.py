milk=0.5
hours=[]
total=0
for i in range(7):
    home=int(input("how many hours were you at home?"))
    hours.append(home)
for item in(hours):
    total=total+((item*milk)*1.35)
print(round(total,2))