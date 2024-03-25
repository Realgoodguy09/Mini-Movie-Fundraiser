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

# loop for testing
while True:

    # Get age (assume users input is a valid integer)
    age = int(input("Age: "))

    # caculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket: ${:.2f}".format(age, ticket_cost))
    