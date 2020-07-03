# PYTHON CRASH COURSE
# Chapter 10: Files and Exceptions

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

# 10-9 Silent Cats and Dogs
with open("C:/Users/angel/Downloads/package/messages/695982619917025300/messages.txt", encoding="utf-8") as f:
    contents = f.read()
    ngl = contents.count("ngl")
    print(ngl)
