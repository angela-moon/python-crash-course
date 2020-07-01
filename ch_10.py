# PYTHON CRASH COURSE
# Chapter 10: Files and Exceptions

# 10-1 Learning Python
with open("10-1.txt") as file_object:
    """contents = file_object.read()
    print(contents)
    for line in file_object:
        print(line)"""
    lines = file_object.readlines()
"""
for stripe in lines:
    print(stripe)"""


# 10-2 Learning C

for line in lines:
    print(line.replace("Python", "C"))

