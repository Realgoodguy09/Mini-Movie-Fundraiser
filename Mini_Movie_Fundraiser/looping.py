# main routine goes here

# set maximum number of tickest below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
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