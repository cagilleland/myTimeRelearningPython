#Loan Calculator App

from matplotlib import pyplot

def get_loan_info():
    loan = {}
    loan['principle'] = float(input("Enter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: "))/100
    loan['monthly payment'] = float(input("Enter the desired monthly payment: "))
    loan['money paid'] = 0
    return loan

def show_loan_info(loan_dict,month_num):
    print("Loan info after " + str(month_num) + " months.")
    for key, value in loan_dict.items():
        print(key.title() + ": " + str(value))

def collect_interest(loan_dict):
    loan_dict['principle'] = loan_dict['principle']+loan_dict['principle']*loan_dict['rate']/12

def make_monthly_payment(loan_dict):
    loan_dict['principle'] = loan_dict['principle'] - loan_dict['monthly payment']
    if loan_dict['principle']>0:
        loan_dict['money paid'] += loan_dict['monthly payment']
    else:
        loan['money paid'] += loan['monthly payment'] + loan['principle']
        loan['principal'] = 0

def summerize_loan(loan_dict, month_num, initial_principle):
    print("Loan paid off in " + str(month_num) + ' months')
    print("Initial loan was $" + str(initial_principle) + " at a rate of " + str(100*loan_dict['rate']))
    print("Monthly payment was $" + str(loan_dict['monthly payment']) + "per month")
    print("Total spent was $" + str(round(loan_dict['money paid'],2)))
    interest = round(loan_dict['money paid']-initial_principle,2)
    print("You spent $" + str(interest) + " in interest")

def create_graph(data,loan):
    x_values = []
    y_values = []
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
    pyplot.plot(x_values,y_values)
    pyplot.title(str(100*loan['rate']) + "% Interest With $" + str(loan['monthly payment']) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()

print("Welcome to the Loan Calculator App")
month_number = 0
loan = get_loan_info()
starting_principle = loan['principle']
data_to_plot = []
show_loan_info(loan,0)
input("Press ENTER to begin paying off loan.")

while loan['principle'] > 0:
    if loan['principle'] > starting_principle:
        break
    month_number +=1
    collect_interest(loan)
    make_monthly_payment(loan)
    data_to_plot.append((month_number,loan['principle']))
    show_loan_info(loan,month_number)

if loan['principle'] <= 0:
    summerize_loan(loan,month_number,starting_principle)
    create_graph(data_to_plot, loan)

else:
    print("You will never pay off the loan.")
