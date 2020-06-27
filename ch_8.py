# PYTHON CRASH COURSE
# Chapter 8: FUnctions

# 8-1 Message
def display_message():
    print("i am learning lots, trust me")

display_message()

# 8-2 Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")

favorite_book("the giver")

# 8-3 T-Shirt
def make_shirt(size, message):
    print(f"The size of your t-shirt is: {size.title()}.")
    print(f"The message on your t-shirt is: '{message}'.")

make_shirt("small", "wow i have a cool shirt")
make_shirt(message="yes this is a cool shirt", size="medium")

# 8-4 Large Shirts
def make_shirt2(size="Large", message="I love Python"):
    print(f"You have ordered a {size} t-shirt with the message '{message}'.")
make_shirt2()
make_shirt2(size="Medium")
make_shirt2(size="Small", message="I love Java")

# 8-5 Cities
def describe_city(city, country="United States of America"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("Nashua")
describe_city("New York City")
describe_city("London", "England")

# 8-6 City Names
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country("Paris", "France")
city_country("New York City", "United States of America")
city_country("Seoul", "South Korea")

# 8-7 Album
def make_album(artist, album, num_songs=None):
    new_album = {
        "artist": artist,
        "album": album,
        "number of songs": num_songs
    }
    return new_album

neo_zone = make_album("NCT 127", "NCT #127 Neo Zone")
awaken_the_world = make_album("WayV", "WayV The 1st Album 'Awaken the World'")
go_live = make_album("Stray Kids", "Go Live")
print(f"{neo_zone}\n{awaken_the_world}\n{go_live}")

reload = make_album("NCT DREAM", "Reload", num_songs=6)
print(reload)

# 8-8 User Albums
while True:
    in_artist = input("Enter the album's artist: (Please enter 'q' to quit.) ")
    if in_artist == "q":
        break
    in_album = input("Enter the album's title: (Please enter 'q' to quit.) ")
    if in_album == "q":
        break

    new_album = make_album(in_artist, in_album)
    print(new_album)

# 8-9 Messages
msgs = ["yello", "yai", "yow ya yoin'", "yis yis ya yessage"]

def show_messages(messages):
    for message in messages:
        print(message)

# show_messages(msgs)

# 8-10 Sending Messages
sent_messages = []

def send_messages(to_be_sent):
    while to_be_sent:
        sending = to_be_sent.pop()
        print(sending)
        sent_messages.append(sending)

# send_messages(msgs)

# 8-11 Archived Messages
send_messages(msgs[:])
print(msgs)

# 8-12 Sandwiches
def make_sandwich(*items):
    print(f"Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("bacon", "lettuce", "tomato")
make_sandwich("egg", "ham")
make_sandwich("chicken")

# 8-13 User Profile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("bro", "is", crash_course= "trying to get my info", fav_color= "blue", clock= "ticking")
print(user_profile)

# 8-14 Cars
def make_car(manufacturer, model_name, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs

car1 = make_car("subaru", "outback", color="blue", tow_package=True)
print(car1)
