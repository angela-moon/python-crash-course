# CRASH COURSE PYTHON
# Chapter 6: Dictionaries

# 6-1 Person
person = {'first_name': 'tape', 'last_name': 'measure', 'city': 'concord'}
print(person)

# 6-2 Favorite Numbers
fav_num = {'tape': '7', 'ace': '24', 'xavier': '0'}
print(f"Tape's favorite number is {fav_num['tape']}.")
print(f"Ace's favorite number is {fav_num['ace']}")
print(f"Xavier's favorite number is {fav_num['xavier']}")

# 6-3 Glossary
cs_dict = {'os': 'Operating System', 'cs': 'Computer Science', 'variable': 'A way to abbreviate longer,'
                                                                           'repeated lines of code',
           'string': 'A datatype that consists of characters separated from code by quotes', 'float':
           'A datatype that consits of a number with a decimal point', 'boolean': 'A datatype that '
                                                                                  'consists of two'
                                                                                  'possible values: '
                                                                                  'True and False',
           'dictonary': 'This is a dictionary'}

"""print(f"OS: {cs_dict['os'].title()}\n")
print(f"CS: {cs_dict['cs'].title()}\n")
print(f"Variable: {cs_dict['variable']}\n")
print(f"String: {cs_dict['string']}\n")
print(f"Float: {cs_dict['float']}\n")"""

# 6-4 Glossary 2
for key, value in cs_dict.items():
    print(f"{key.title()}: {value}\n")

# 6-5 Rivers
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
names = ['jen', 'phil', 'lisa', 'brendan']
for name in names:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please fill out the poll.")

# 6-7 People


# 6-8 Pets


# 6-9 Favorite Places


# 6-10 Favorite Numbers


# 6-11 Cities


# 6-12 Extensions