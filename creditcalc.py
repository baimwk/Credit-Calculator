import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type", dest="type_of_payment", type=str, choices=["diff", "annuity"], required=True)
parser.add_argument("--periods", dest="period_count", type=int, required=False)
parser.add_argument("--payment", dest="monthly_payment", type=float, required=False)
parser.add_argument("--interest", dest="credit_interest", type=float, required=False)
parser.add_argument("--principal", dest="credit_principal", type=float, required=False)

args = parser.parse_args()


if args.type_of_payment == 'diff' and args.credit_interest is not None and args.period_count is not None:
    nominal_interest = args.credit_interest / (12 * 100)
    if args.type_of_payment == 'diff':
        sum_diff_payments = 0
        for i in range(1, args.period_count + 1):
            montly_diff_payment = math.ceil(args.credit_principal / args.period_count + nominal_interest * (
            args.credit_principal - args.credit_principal * (i - 1) / args.period_count))
            sum_diff_payments += montly_diff_payment
            print(f"Month {i}: payment is {montly_diff_payment}")
        print("\nOverpayment =", int(sum_diff_payments - args.credit_principal))
elif args.type_of_payment == 'annuity' and args.monthly_payment is not None and args.period_count is not None and args.credit_interest is not None:
    nominal_interest = args.credit_interest / (12 * 100)
    credit = math.floor(args.monthly_payment / ((nominal_interest * math.pow(1 + nominal_interest, args.period_count)) / (math.pow(1 + nominal_interest, args.period_count) - 1)))
    print(f"Your credit principal = {credit}!")
    print("Overpayment = ", math.ceil(args.monthly_payment * args.period_count - credit))
elif args.type_of_payment == 'annuity' and args.credit_principal is not None and args.monthly_payment is not None and args.credit_interest is not None:
    nominal_interest = args.credit_interest / (12 * 100)
    months = math.ceil(math.log(args.monthly_payment / (args.monthly_payment - nominal_interest * args.credit_principal), 1 + nominal_interest))
    years = months // 12
    months = months % 12
    if months != 0:
        print(f"I will take {years} years and {months} months to repay this credit!")
    else:
        print(f"I will take {years} ", "years" if years > 1 else "year", "to repay this credit!")
        print("Overpayment =", int(args.monthly_payment * (years * 12 + months) - args.credit_principal))
elif args.type_of_payment == 'annuity' and args.credit_principal is not None and args.period_count is not None and args.credit_interest is not None:
    nominal_interest = args.credit_interest / (12 * 100)
    annuity = math.ceil(args.credit_principal * (nominal_interest * math.pow(1 + nominal_interest, args.period_count) / (math.pow(1 + nominal_interest, args.period_count) - 1)))
    print(f"Your annuity payment =  {annuity}!")
    print("Overpayment =", int(annuity * args.period_count - args.credit_principal))
else:
    print('Incorrect parameters.')
