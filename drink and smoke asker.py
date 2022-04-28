smoke_quantity=0
smoke_year=0
drink_quantity=0
drink_year=0
d_years=0
s_years=0

age=int(input("what is your age?"))
gender=input("are you male or female?(M/F):")

while True:
    smoke = input("Do you smoke?(Y/N):")
    if smoke=="Y"or"N":
        break
    else:
        print("invalid input")
while True:
    drink = input("Do you drink alchol?(Y/N):")
    if drink=="Y"or"N":
        break
    else:
        print("invalid input")

if smoke=="Y":
    smoke_quantity=float(input("How many cigs do you smoke a day?:"))
    if smoke_quantity>10:
        print("you have an increased risk of lung cancer")
    smoke_year=smoke_quantity*365.25
    s_years=int(input("how many years have you been smoking?"))
    
if drink=="Y":
    drink_quantity=float(input("How many units of alchol do you drink a day?:"))
    if drink_quantity<4:
        print("you are so uncool")
    drink_year=drink_quantity*365.25
    d_years=int(input("how many years have you been drinking?"))
print("you drink",drink_year,"units of alchol a year and smoke",smoke_year,"cigs a year")



drink_total=(d_years*drink_year)*9
smoke_total=(s_years*smoke_year)*12



if gender=="M":
    male_min=525600*78
    y_lost=male_min-drink_total-smoke_total
    y_left=78-age
    print("you have",(y_left-y_lost)/525600,"left to live")
else:
    female_min=525600*82
    y_lost=female_min-drink_total-smoke_total
    y_left=82-age
    print("you have",(y_left-y_lost)/525600,"left to live")
    
    





