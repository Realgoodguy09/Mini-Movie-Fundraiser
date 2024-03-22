# used to print spaces between each restart / run
print()
print()
print()
print()

# functions go here
def cash_credit(question):


    while True:
        response = input(question).lower()

        if response == 'cash' or response == 'ca':
            return 'cash'

        elif response == 'credit' or response == 'cr':
            return 'credit'

        else:
            print('Please enter a valid payment method')

# main routine goes here


payment_method = cash_credit('Choose a payment method (cash or credit): ')


if payment_method == "yes":
    print("Instructions go here")

print('We are done')