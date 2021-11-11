def bmi_model():
    while True:
        try:
            height_cm= float(input("how tall are you in cm?: "))
            weight= float(input("What is your weight in kgs?: "))
        except ValueError:
            print("invalid input")
        else:
            break
    height_m = height_cm/100
    bmi=round(height_m/(weight**2),)
    print("your bmi is: ",bmi)
    
    if bmi<18.5:
        print("You are under weight")
    elif bmi>=18.5 and bmi<=29.9:
        print("You are a normal weight")
    elif bmi>=25 and bmi<=24.9:
        print("You are overweight")
    elif bmi>=30:
        print("You are obese")