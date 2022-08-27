
import math
import argparse
parser = argparse.ArgumentParser(description="Well, I don't know")
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--principal")
args = parser.parse_args()

if args.interest == None or args.type == None or (args.payment != None and args.periods != None and args.principal != None):
    print("Incorrect Parameters")
else:
    
    interest = float(args.interest)
        
        
    if args.type == "annuity":
        if args.principal != None and args.periods != None:
            periods = float(args.periods)
            principal = float(args.principal)
            if periods < 0 or principal < 0:
                print("Incorrect Parameters")
            else:
                nominal_interest_rate = interest / (12 * 100)
                i = nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)
                j = math.pow(1 + nominal_interest_rate, periods) - 1
                Annuity_payment = principal * (i / j)
                Annuity_payment = math.ceil(Annuity_payment)
                principal = math.ceil(principal)
                print(f"Your annuity payment is = {Annuity_payment}!")
                # print(f"Overypayment = {principal - Annuity_payment}")
            
        elif args.payment != None and args.periods != None:
            payment = float(args.payment)
            periods = float(args.periods)
            
            if periods < 0 or payment < 0:
                print("Incorrect Parameters")
            else:
                nominal_interest_rate = interest / (12 * 100)
                i = nominal_interest_rate * (math.pow(1 + nominal_interest_rate, periods))
                j = math.pow(1 + nominal_interest_rate, periods) - 1
                loan_principal = payment * (j / i)
                a = math.ceil(loan_principal)
                print(f"Your loan principal is = {a}!")
                tot_payment = payment * periods
                tot_payment = math.ceil(tot_payment)
                print(f"Overpayment = {tot_payment - loan_principal}")
        
        else:
            principal = float(args.principal)
            payment = float(args.payment)
            
            if payment < 0 or principal < 0:
                print("Incorrect Parameters")
            else:
                nominal_interest_rate = interest / (12 * 100)
                no_of_months = math.log(payment / (payment - nominal_interest_rate * principal), 1 + nominal_interest_rate)
                a = math.ceil(no_of_months)
                total_payment = payment * a
                total_payment = math.ceil(total_payment)
                if a > 12:
                    years, months = divmod(a, 12)
                    if months == 0:
                        print(f"It will take {years} years to repay this loan!")
                    else:
                        print(f"It will take {years} years and {months} months to repay this loan!")
                else:
                    print(f"It will take {months} months to repay this loan!")
                print(f"Overpayment = {total_payment - principal}")         
        
        
        
    elif args.type == "diff":
        if args.payment != None:
            print("Incorrect Parameters")
        else:
            if args.principal != None and args.periods != None:
                periods = int(args.periods)
                principal = float(args.principal)
                
                if periods < 0 or principal < 0:
                    print("Incorrect Parameters")
                else:
                    nominal_interest_rate = interest / (12 * 100)
                    total_payment = 0
                    for i in range(0, periods):
                        this_month_pay = principal / periods + nominal_interest_rate * (principal - (principal * i) / periods)
                        this_month_pay = math.ceil(this_month_pay)
                        print(f"Month {i}: payment is {this_month_pay}")
                        total_payment += this_month_pay
                    principal  = math.ceil(principal)    
                    print(f"Overpayment = {total_payment - principal}")
