# CRASH COURSE PYTHON
# Chapter 5: If Statements

# 5-1 Conditional Tests
color = 'blue'
print("Is color == 'blue'? I predict True.")
print(color == 'blue')
print("Is color == 'red'? I predict False.")
print(color == 'red')

day = 'wednesday'
print("Is it a Wednesday, my dudes? I bet it is a Wednesday, my dudes.")
print(day == 'wednesday')
print("Is it a Thurdsday, my dudes? I bet it is not a Thursday, my dudes.")
print(day == 'thursday')

num = 24
print("Is the number 24? I predict True.")
print(num == 24)
print("Is the number 42? I predict False.")
print(num == 42)

texture = 'plaid'
print("Is the texture plaid? I predict True.")
print(texture == 'plaid')
print("Is the texture dotted? I predict False.")
print(texture == 'dotted')

animal = 'bear'
print('Is the animal a bear? I predict True.')
print(animal == 'bear')
print("Is the animal a cat? I predict False.")
print(animal == 'cat')

# 5-2 More Conditional Tests
#  Test using the lower() method
day = 'WEDnesDaY'
if day.lower() == 'wednesday':
    print(f"It is a {day.title()}, my dudes!")
else:
    print("It is not a {day.title()} my dudes :(")

#  Numerical tests involving grater than and less than, greater than or equal 
#  to, and less than or equal to
if num <= 30:
    print("smol num")
elif num <= 150:
    print("medium num")
elif num >= 151:
    print("swol number")
else: 
    print("sir, is this a number..?")
    
#  Tests using the and keyword and the or keyword
num1 = 4
num2 = 7
print(num1 >= 2 and num2 >= 2)
print(num1 <= 2 and num2 <= 2)
print(num1 >= 6 or num2 >= 6)
print(num1 >=10 or num2 >= 10)

#  Test whether an item is in a list
wow_list = ['wow', 'yoo', 'dangg', 'ayee']
for wow in wow_list:
    if wow == 'wow':
        print(f"the wow is in the wow list wow")
    else:
        print(wow)
        
#  Test whether an item is not in a list
bad = ['you', 'me', 'the letter x']
pros_bad = 'you'
if pros_bad not in bad:
    print(f"{pros_bad} does not pass the vibe check")
else:
    print(f"{pros_bad} pass the vibe check.")
    
# 5-3 Alien Colors #1
alien_color = 'red'
if alien_color == 'green':
    print('You have earned five points!')
else:
    print(" ")

# 5-4 Alien Colors #2
if alien_color == 'green':
    print('You have earned five points!')
else:
    print('You have earned ten points!')

# 5-5 Alien Colors #3
if alien_color == 'green':
    print('You have earned five points!')
elif alien_color == 'yellow':
    print('You have earned ten points!')
elif alien_color == 'red':
    print('You have earned fifteen points!')

# 5-6 Stages of Life
    age = 0
    if age < 2:
        print("You are a baby.")
    elif age < 4:
        print("You are a toddler.")
    elif age < 13:
        print("You are a kid.")
    elif age < 20:
        print("You are a teen.")
    elif age < 65:
        print("You are an adult.")
    elif age >= 65:
        print("You are an elder.")

# 5-7 Favorite Fruit
fav_fruits = ['peaches', 'strawberries', 'blueberries']
if 'peaches' in fav_fruits:
    print("You must like peaches!")
if 'strawberries' in fav_fruits:
    print("You must like strawberries!")
if 'blueberries' in fav_fruits:
    print("You must like blueberries!")
if 'apples' in fav_fruits:
    print("You must like apples!")
if 'oranges' in fav_fruits:
    print("You must like oranges!")

# 5-8 Hello Admin (perhaps i do simp for minecraft youtubers...)
usernames = ['admin', 'dream', 'georgeNotFound', 'sapnap', 'BadBoyHalo']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {username.upper()}, welcome back to Minecraft.")
# 5-9 No Users
else:
    print("We need to find some users!")

# 5-10 Checking Usernames
current_users = ['WOwiE', 'what a username', 'dream', 'imnewheredontattackme', 'royally flushed']
lower_users = []
for current_user in current_users:
    lower_users.append(current_user.lower())
new_users = ['wowie', 'imnewheredontattackme', 'pythonnoob', 'welp', 'sprite']
for new_user in new_users:
    if new_user.lower() in lower_users:
        print("That username has already been used. Please type in a new username.")
    else:
        print("That username is available!")

# 5-11 Ordinal Numbers
ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in ordinals:
    if num == 1:
        print("1st\n")
    elif num == 2:
        print("2nd\n")
    elif num == 3:
        print("3rd\n")
    elif num <= 9:
        print(f"{num}th\n")
