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
    name = input("Please enter your name or 'xxx' to quit: ")


    if name == 'xxx':
        break


    tickets_sold += 1


# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all of the tickets")
else:
    print("you have sold {} ticket/s. There is {} tickets remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))