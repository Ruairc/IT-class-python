#Q4 pg189
day=input("is it a weekday or weekend?(day/end)")
motor=int(input("what is the power of the motor you are renting(50/250)"))

if motor==50:
    if day=="end":
        print("ITS $30 FOR THE FIRST THREE HOURS THEN $3 FOR EVERY HOUR AFTER")
    elif day=="day":
        print("ITS $15 FOR THE FIRST THREE HOURS THEN $2.50 FOR EVERY HOUR AFTER")
    else:
        print("invalid")
else:
    if day=="end":
        print("ITS $35 FOR THE FIRST THREE HOURS THEN $5 FOR EVERY HOUR AFTER")
    elif day=="day":
        print("ITS $25 FOR THE FIRST THREE HOURS THEN $3.50 FOR EVERY HOUR AFTER")
    else:
        print("invalid")
        