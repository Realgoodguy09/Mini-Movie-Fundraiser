# functions go here

# Checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'

        elif response == 'no' or response == 'n':
            return 'no'

        else:
            print('Please enter yes / no')

# Checks users response is not blank
def not_blank(question): 


    while True:
        response = input(question)

        # If response is blank, outputs error
        if response == '':
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# Checks the user enters an integer to a given question
def num_checker(question):

    while True:
        
        try:
            response = int(input(question))
            return response



        except ValueError:
            print("Please enter an integer.")



# Calculate the ticket price based 
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5


    # ticket is $10.50 for users between age 16 and 64
    elif var_age < 65:
        price = 10.5


    # ticket is $6.50 for seniors (65+)
    else:
        price = 6.5
    
    return price

# main routine goes here

# set maximum number of tickest below
MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = yes_no('Do you want to read the instructions? ').lower()


if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")


    if name == 'xxx':
        break

    age = int(input("Age: "))

    if 12<= age <= 120:
        pass
    elif age < 12:
        print("Sorry, you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    # caculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket: ${:.2f}".format(age, ticket_cost))
    

    tickets_sold += 1


# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all of the tickets")
else:
    print("you have sold {} ticket/s. There is {} tickets remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))