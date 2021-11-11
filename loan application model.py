#Ruairc's Loan Application code
def loan_application(amount_applied,years,interest, monthly_salary):
    months= years*12
    d_interest=interest/100
    
    total = amount_applied*((d_interest+1)**years)
    repayment_amount= round(total/months,2)
    thirty_of_monthly=monthly_salary*.30
    
    print("Your monthly repayment amount is: €",repayment_amount)
    print("This is 30% of your monthly salary: €",thirty_of_monthly)
    
    if thirty_of_monthly > repayment_amount:
        return "You are eligeable for this loan"
    elif thirty_of_monthly < repayment_amount:
        return "You are not eligeable for this loan"
    
print(loan_application(40000,1,.32,3500))
