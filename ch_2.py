# PYTHON CRASH COURSE
# Chapter 2: Variables and Basic Data Types

# 2-1 Simple Message
# This program takes a string in the variable "message" and prints it.
message = "Hi there. How are you today?"
print(message)

# 2-2 Simple Messages
# This program takes a string in the variable "message" and prints it. Then, a new string is assigned to the
# variable "message" and that string is printed.
message = "How are you?"
print(message)
msg = "I'm doing well."
print(message)

# 2-3 Personal Message
# This program takes a string as a name and prints it in a message that incorporates the name.
name = "justin"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

# 2-4 Name Cases
name = "aNgeLa mOOn"
print(name.upper()) # ANGELA MOON
print(name.lower()) # angela moon
print(name.title()) # Angela Moon

# 2-5 Famous Quote
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

# 2-6 Famous Quote 2
famous_person = "Albert Einstein"
message = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""
print(message)

# 2-7 Stripping Names
name = "   \tAngela Moon \n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2-8 Number Eight
print(4 * 2) # 8
print (13 - 5) # 8
print(1 + 7) # 8
print(int(16/2)) # 8.0 -> 8

# 2-9 Favorite Number
fav_num = 24
message = f"My favorite number is {fav_num}. What is your favorite number?"
print(message)



