def temp_model(start_temp):
    while True:
        try:
            time_of_day=int(input("what time is it?(numbers only,using 24 hr clock): "))
        except ValueError:
            print("invalid input")
        else:
            break
        break

    if time_of_day<12:
        return start_temp+time_of_day
    elif time_of_day==12:
        return start_temp+11
    else:
        return (start_temp+11)-(-12)
print("the temperature should be:",temp_model(5))