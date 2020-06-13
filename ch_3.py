# PYTHON CRASH COURSE
# Chapter 3: Introducing Lists

# 3-1 Names
names = ['angela', 'justin', 'mom', 'dad']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2 Greetings
print(f"Hello, {names[0].title()}.")
print(f"Hello, {names[1].title()}.")
print(f"Hello, {names[2].title()}.")
print(f"Hello, {names[3].title()}.")

# 3-3 Your Own List
colors = ['blue', 'purple', 'pink', 'yellow', 'orange']
print(f"My favorite color {colors[0]}!")
print(f"I like {colors[1]} a little bit.")
print(f"I think {colors[2]} is cool.")
print(f"{colors[3].title()} is very bright, but pretty when muted.")
print(f"{colors[4].title()} is an odd color.")

# 3-4 Guest List
guests = ['linda', 'bob', 'lisa', 'brendan']
print(f"{guests[0].title()}, you are cordially invited to my dinner party.")
print(f"{guests[1].title()}, you are cordially invited to my dinner party.")
print(f"{guests[2].title()}, you are cordially invited to my dinner party.")
print(f"{guests[3].title()}, you are cordially invited to my dinner party.")

# 3-5 Changing Guest List
print(f"Unfortunately, {guests[1].title} is unable to make it to your dinner party.")
guests[1] = 'side hoe of linda'
print(f"{guests[0].title()}, you are cordially invited to my dinner party.")
print(f"{guests[1].title()}, you are cordially invited to my dinner party.")
print(f"{guests[2].title()}, you are cordially invited to my dinner party.")
print(f"{guests[3].title()}, you are cordially invited to my dinner party.")

# 3-6 More Guests
print("We have found a larger table!")
guests.insert(0, 'chewsday')
guests.insert(3, 'no it is tuesday, karen')
guests.append('wot')
print(f"{guests[0].title()}, you are cordially invited to my dinner party.")
print(f"{guests[1].title()}, you are cordially invited to my dinner party.")
print(f"{guests[2].title()}, you are cordially invited to my dinner party.")
print(f"{guests[3].title()}, you are cordially invited to my dinner party.")
print(f"{guests[4].title()}, you are cordially invited to my dinner party.")
print(f"{guests[5].title()}, you are cordially invited to my dinner party.")
print(f"{guests[6].title()}, you are cordially invited to my dinner party.")

# 3-7 Shrinking Guest List
print("Ah, sorry for yet another inconvenience. Only two of the best guests may continue to the new, limited space "
      "table.")
bad_guests = guests.pop()
print(f"{bad_guests.title()}, you have been ejected from the table.")
bad_guests = guests.pop()
print(f"{bad_guests.title()}, you have been ejected from the table.")
bad_guests = guests.pop()
print(f"{bad_guests.title()}, you have been ejected from the table.")
bad_guests = guests.pop()
print(f"{bad_guests.title()}, you have been ejected from the table.")
bad_guests = guests.pop()
print(f"{bad_guests.title()}, you have been ejected from the table.")
print(f"{guests[0].title()} and {guests[1].title()} you are cordially invited to my dinner party.")
del guests[1]
del guests[0]
print(guests)

# 3-8 Seeing the World
travel = ['seoul', 'rome', 'antarctica', 'california', 'canada']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel, reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

# 3-9 Dinner Guests
print(len(guests))
print(len(bad_guests))

# 3-10 Every Function
reds = ['INDIAN RED', 'LIGHT CORAL', 'SALMON', 'DARK SALMON', 'LIGHT SALMON', 'CRIMSON', 'RED', 'FIRE BRICK',
        'DARK RED']
print(f"These are the first three HTML RED colors: {reds[0].title()}, {reds[1].title()}, and {reds[2].title()}")
print(f"The full list is: {reds}")
print(len(reds))
reds.append('CORAL')
reds.append('TOMATO')
print(f"I added some colors that are in the orange color family, but are still red: {reds[9].title()} and "
      f"{reds[10].title()}")
reds.insert(2, 'PEACHPUFF')
reds.insert(3, 'MOCCASIN')
print(f"Here are some lighter red colors that I thought should be added: {reds[2].title()} and {reds[3].title()}")
reds.sort()
reds_too_long = reds.pop()
print(reds)
print(reds_too_long)
reds.remove('INDIAN RED')
del reds[5]
print(f"The list was too long, so I removed {reds_too_long.title()}. I also deleted"
      f" some more just for fun.")
print(reds)
print(sorted(reds, reverse=True))


