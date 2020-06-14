import math
import argparse
import sys


ap = argparse.ArgumentParser()
# ap.add_argument("--type", "--principal", "--periods", "--interest", "--payment")
ap.add_argument("--type", required=True,
                help="Enter values...")
ap.add_argument("--principal", type=float,
                help="Enter values...")
ap.add_argument("--periods", type=float,
                help="Enter values...")
ap.add_argument("--interest", type=float,
                help="Enter values...")
ap.add_argument("--payment", type=float,
                help="Enter values...")
arg_num = len(sys.argv)
args = vars(ap.parse_args())
# args = parser.parse_args()


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
    return math.floor(numerator / (sub_numerator / sub_denominator))


# n interest, annuity, principal
def calc_num_of_payments(i, a, p):
    nominal_interest = calc_nom_int_rate(i)
    return math.ceil(math.log(a / (a - nominal_interest * p), (1 + nominal_interest)))


# i
def calc_nom_int_rate(i):
    return (i * .01) / 12


# Dm
def calc_diff_payment(inter, m_current_period, n_payments, p_principal_total):
    nominal_interest = calc_nom_int_rate(inter)
    first = p_principal_total / n_payments
    second = nominal_interest * (p_principal_total - (p_principal_total * ((m_current_period - 1) / n_payments)))
    return math.ceil(first + second)


if arg_num < 4:
    print("Incorrect parameters")
    # print("Less than 4 args")
elif args["type"] == "annuity":
    if args["interest"] and args["payment"] and args["periods"]:
        principal = calc_credit_principal(args["payment"], args["periods"], args["interest"])
        print(f"Your credit principal = {principal}")
    elif args["interest"] and args["payment"] and args["principal"]:
        payments = calc_num_of_payments(args["interest"], args["payment"], args["principal"])
        if payments > 11:
            years = payments // 12
            months = payments % 12
            if months != 0:
                print(f"You need {years} years and {months} months to repay this credit!")
            else:
                print(print(f"You need {years} years to repay this credit!"))
        elif payments < 1:
            print(f"You need {payments} months to repay this credit!")
        else:
            print(f"You need {payments} month to repay this credit!")
        total_paid = args["payment"] * payments
        overpayment = total_paid - args["principal"]

        print(f"Overpayment = {overpayment}")
    elif args["interest"]:
        payment_amount = calc_ordinary_annuity(args["principal"], args["interest"], args["periods"])
        print(f"Your annuity payment = {payment_amount}")
    else:
        print("Incorrect parameters")
elif args["type"] == "diff":
    if args["payment"]:
        print("Incorrect parameters")
    else:
        # Calc
        total_paid = 0
        month_counter = 1
        while total_paid < args["principal"]:
            diff = calc_diff_payment(args["interest"], month_counter, args["periods"], args["principal"])
            print(f"Month {month_counter}: paid out {diff}")
            month_counter += 1
            total_paid += diff
        overpayment = total_paid - args["principal"]
        print(f"Overpayment = {overpayment}")
else:
    print("Incorrect parameters")
    print("Wrong Types")


#
# options = input("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:
# """)
#
# if options == "n":
#     credit_principal = float(input("Enter credit principal:"))
#     annuity_payment = float(input("Enter monthly payment:"))
#     interest_rate = float(input("Enter credit interest:"))
#     no_payments = calc_num_of_payments(interest_rate, annuity_payment, credit_principal)
#     if no_payments > 11:
#         years = no_payments // 12
#         months = no_payments % 12
#         print(f"You need {years} years and {months} months to repay this credit!")
#     elif no_payments < 1:
#         print(f"You need {no_payments} months to repay this credit!")
#     else:
#         print(f"You need {no_payments} month to repay this credit!")
# elif options == "a":
#     credit_principal = float(input("Enter credit principal:"))
#     periods = float(input("Enter count of periods:"))
#     interest_rate = float(input("Enter credit interest:"))
#     monthly = calc_ordinary_annuity(credit_principal, interest_rate, periods)
#     print(f"Your annuity payment = {monthly}")
# else:
#     annuity_payment = float(input("Enter monthly payment:"))
#     periods = float(input("Enter count of periods:"))
#     interest_rate = float(input("Enter credit interest:"))
#     principal = calc_credit_principal(annuity_payment, periods, interest_rate)
#     print(f"Your credit principal = {principal}!")
