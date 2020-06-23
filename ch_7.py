# CRASH COURSE PYTHON
# Chapter 7: User Input and While Loops

# 7-1 Rental Car
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car.title()}")

# 7-2 Restaurant Seating
table = input("How many people are in your dinner group? ")
if int(table) >= 8:
    print("Please wait for a table to be ready.")
else:
    print("Your table is ready.")

# 7-3 Multiples of Ten
num = input("Please enter an integer: ")
if int(num) % 10 == 0:
    print("That number is a multiple of ten.")
else:
    print("That number is not a multiple of ten.")

# 7-4 Pizza Toppings
active = True
while active:
    pizza = input("Enter a pizza topping: \n (Enter 'quit' to stop the program) ")

    if pizza == "quit":
        active = False
    else:
        print(f"I will add {pizza.lower}.")


# 7-5 Movie Tickets
# under 3, free. 3-12, 10. over 12, 15.
party = input("How many members are a part of your party? ")
num = 0
while int(party) > num:
    ticket = input("How old is a member of your party? ")
    if int(ticket) < 3:
        print("Your ticket is free.")
    elif int(ticket) <= 12:
        print("Your ticket is $10.")
    elif int(ticket) > 12:
        print("Your ticket is $15.")
    num = num + 1

# 7-8 Deli
sandwich_orders = ['peanut butter and jelly', 'panini', 'what is another sandwich', 'breakfast',
                   'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

# 7-9 No Pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I have made your {current.title()}!")
    finished_sandwiches.append(current)

print(f"\n Complete Sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-10 Dream Vacation
responses = {}
active = True

while active:
    name = input("\nName: ")
    response = input("If you could visit one place in the workd, where would you go? ")
    responses[name] = response

    repeat = input("Will someone take this poll after you? (y/n) ")
    if repeat == "n":
        active = False

print("\n --- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}.")
