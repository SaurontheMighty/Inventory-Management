#Movie Ticket Cost Calculator

#Initializing Variables
ticket_cost = 0
adult_tickets = 0
child_tickets = 0
senior_tickets = 0
while_counter = 0

#To buy tickets
while(while_counter==0):
    print(" ")
    response = input("Do you want to purchase a ticket? (Y/N) ")
    if(response=="Y" or response=="y"):
        age = int(input("Enter age of customer: "))
        if age in range(14,65):
            adult_tickets+=1
            ticket_cost+=12
            print("Ticket added to cart")
        if age in range(0,14):
            child_tickets+=1
            ticket_cost+=8
            print("Ticket added to cart")
        if(age>=65):
            senior_tickets+=1
            ticket_cost+=6
            print("Ticket added to cart")
    else:
        while_counter = 1

#To print number of tickets      
print("Number of Adult Tickets: ",adult_tickets)
print("Number of Child Tickets: ",child_tickets)
print("Number of Senior Tickets: ",senior_tickets)
print("Ticket Cost: ",ticket_cost)

#To calculate total price
tax=0.13*ticket_cost
print("Tax: ",tax)
total = ticket_cost+tax
print("Total: ",total)
