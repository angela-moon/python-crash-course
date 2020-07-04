# PYTHON CRASH COURSE
# Chapter 10: Files and Exceptions

import json

# 10-1 Learning Python
"""with open("ch_10.txt") as file_object:
    contents = file_object.read()
    print(contents)
    for line in file_object:
        print(line)
    lines = file_object.readlines()

for stripe in lines:
    print(stripe)


# 10-2 Learning C

for line in lines:
    print(line.replace("Python", "C"))"""

# 10-3 Guest

filename = 'ch_10.txt'
"""guest = input("Enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(guest)

# 10-4 Guest Book
num = 0

with open(filename, 'w') as file_object:
    while num < 10:
        file_object.write(f"{input('Enter your name: ')}\n")
        num += 1

# 10-5 Programming Poll
num = 0
with open(filename, "w") as file_object:
    while num < 5:
        file_object.write(f"{input('Why do you like programming? ')}\n")
        num += 1"""

# 10-6 Addition

# while True:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    sum = num1 + num2
except ValueError:
    print("Error")
else:
    print(sum)

# 10-8 Cats and Dogs
try:
    with open("ch_10.txt", "r") as file_object:
        for line in file_object:
            print(f"{line}")
except FileNotFoundError:
    pass

# 10-10 Common Words
with open("C:/Users/angel/Downloads/package/messages/695982619917025300/messages.txt", encoding="utf-8") as f:
    contents = f.read()
    ngl = contents.count("ngl")
    print(ngl)

# 10-11 Favorite Number


filename = "ch_10.json"
"""with open(filename, "w") as f:
    json.dump(fav_num, f)

with open(filename) as f:
    num = json.load(f)
    print(f"Favorite number is {num}?")"""

# 10-12 Favorite Number Remembered
try:
    with open(filename) as f:
        num = json.load(f)
except FileNotFoundError:
    fav_num = input("Enter your favorite number: ")
    with open(filename, "w") as f:
        json.dump(fav_num, f)
else:
    print(f"Favorite number is {num}?")

# 10-13 Verify User

def get_stored_username():
    filename = "ch_10.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = "ch_10.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    print(username)
    if username:
        is_right_username = input("Is this your username? (yes/no) ")
        if is_right_username == "yes":
            print(f"Welcome back, {username}!")
        else:
            get_new_username()
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()