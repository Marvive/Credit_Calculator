import math


# A principal, interest, number of payments
def calc_ordinary_annuity(p, i, n):
    nominal_interest = calc_nom_int_rate(i)
    return math.ceil(p * (nominal_interest * (1 + nominal_interest) ** n) / (((1 + nominal_interest) ** n) - 1))


# P annuity payments, number of payments, interest rates
def calc_credit_principal(a, n, i):
    nominal_interest = calc_nom_int_rate(i)
    numerator = a
    sub_numerator = nominal_interest * ((1 + nominal_interest) ** n)
    sub_denominator = ((1 + nominal_interest) ** n) - 1
    return numerator / (sub_numerator / sub_denominator)


# n interest, annuity, principal
def calc_num_of_payments(i, a, p):
    nominal_interest = calc_nom_int_rate(i)
    return math.ceil(math.log(a / (a - nominal_interest * p), (1 + nominal_interest)))


# i
def calc_nom_int_rate(i):
    return (i * .01) / 12


options = input("""What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal: 
""")

if options == "n":
    credit_principal = float(input("Enter credit principal:"))
    annuity_payment = float(input("Enter monthly payment:"))
    interest_rate = float(input("Enter credit interest:"))
    no_payments = calc_num_of_payments(interest_rate, annuity_payment, credit_principal)
    if no_payments > 11:
        years = no_payments // 12
        months = no_payments % 12
        print(f"You need {years} years and {months} months to repay this credit!")
    elif no_payments < 1:
        print(f"You need {no_payments} months to repay this credit!")
    else:
        print(f"You need {no_payments} month to repay this credit!")
elif options == "a":
    credit_principal = float(input("Enter credit principal:"))
    periods = float(input("Enter count of periods:"))
    interest_rate = float(input("Enter credit interest:"))
    monthly = calc_ordinary_annuity(credit_principal, interest_rate, periods)
    print(f"Your annuity payment = {monthly}")
else:
    annuity_payment = float(input("Enter monthly payment:"))
    periods = float(input("Enter count of periods:"))
    interest_rate = float(input("Enter credit interest:"))
    principal = calc_credit_principal(annuity_payment, periods, interest_rate)
    print(f"Your credit principal = {principal}!")
