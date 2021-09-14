"""
Name: Caroline Greer
interest.py

Problem: Compute the monthly interest charge on a credit card account

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def main():
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    days_in_billing_period = eval(input("Enter the number of days in the billing period: "))
    previous_net_balance = eval(input("Enter previous net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    day_of_cycle = eval(input("Enter the day of billing cycle payment was made: "))
    step1 = previous_net_balance * days_in_billing_period
    step2 = payment_amount * (days_in_billing_period - day_of_cycle)
    step3 = step1 - step2
    average_daily_balance = step3 / days_in_billing_period
    monthly_interest_rate = annual_interest_rate / 100.0
    monthly_interest_charge = average_daily_balance * (monthly_interest_rate / 12.0)
    print(round(monthly_interest_charge, 2))

if __name__=="__main__":
    main()
