# CRASH COURSE PYTHON
# Chapter 4: Working with Lists

# 4-1 Pizzas
pizzas = ['cheese', 'three cheeses', 'pepperoni']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really like pizza!")

# 4-2 Animals
pets = ['parrot', 'hamster', 'guinea pig', 'kitten', 'puppy']
for pet in pets:
    print(f"I think a {pet} would make a great pet.")
print("Wow. I sure do want to have a pet.")

# 4-3 Counting to Twenty
for value in range(1, 21):
    print(value)

# 4-4 One Million
# it works but im keeping it like this bc it takes a while
million = list(range(1, 1_000_001))
""" for value in million:
     print(value) """

# 4-5 Summing a Million
print(min(million))
print(max(million))
print(sum(million))

# 4-6 Odd Numbers
for value in range(1, 21, 2):
    print(value)

# 4-7 Threes
threes = list(range(3, 31, 3))
for value in threes:
    print(value)

# 4-8 Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
print(cubes)

# 4-9 Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# 4-10 Slices
reds = ['INDIAN RED', 'LIGHT CORAL', 'SALMON', 'DARK SALMON', 'LIGHT SALMON', 'CRIMSON', 'RED', 'FIRE BRICK',
        'DARK RED']
print("The first three items in the list are:")
for red in reds[:3]:
    print(red.title())
print("Two items from the middle of the list are:")
for red in reds[4:6]:
    print(red.title())
print("The last three items in the list are:")
for red in reds[-3:]:
    print(red.title())

# 4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
friend_pizzas.append('yes cheese')
pizzas.append('no cheese')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

# 4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
print("My favorite foods are:")
for food in my_foods:
    print(food.title())

# 4-13 Buffet
menu = ('Fresh Eggs', 'Bacon Bits', 'Sausage Links', 'Homestyle Pancakes', 'Texas Toast')
for item in menu:
    print(item)
# menu[0] = 'Scrambled Eggs' yayyyy errors yayy immutable lists
menu = ('Scrambled Eggs', 'Bacon Bits', 'Sausage Links', 'Homestyle Pancakes', 'Garlic Bread')
for item in menu:
    print(item)