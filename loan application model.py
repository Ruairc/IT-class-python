#Loan Application code
def loan_application(amount_applied,years,interest, monthly_salary):
    months= years*12
    total_interest=0
    total_interest = total_interest+((interest+1)**months)
    repayment_amount = total_interest*amount_applied
    
    
    thirty_of_monthly=monthly_salary*.3
    print(thirty_of_monthly)
    print(repayment_amount)
    if thirty_of_monthly > repayment_amount:
        return 0
    elif thirty_of_monthly < repayment_amount:
        return 1
    
print(loan_application(10000,6,.32,10000))

