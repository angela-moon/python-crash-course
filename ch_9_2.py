# PYTHON CRASH COURSE
# Chapter 9: Classes

# 9-13 Dice

from random import randint, choice

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


num = 0
six_sides = Die(6)

while num <= 10:
    six_sides.roll_die()
    num += 1

# 9-14 Lottery
tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

winner1 = choice(tickets)
winner2 = choice(tickets)
winner3 = choice(tickets)
winner4 = choice(tickets)

winners = [winner1, winner2, winner3, winner4]

print(f"If you have one of the following tickets: {winner1}, {winner2}, {winner3}, or {winner4}, congratulations!"
      f" You win a prize.")

# 9-15 Lottery

ticket = choice(tickets)
print(ticket)
num = 1

while ticket not in winners:
    ticket = choice(tickets)
    print(ticket)
    num += 1

print(f"It took {num} tries to win the lottery.")
