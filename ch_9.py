# PYTHON CRASH COURSE
# Chapter 9: Classes

# 9-1 Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()} is a(n) {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, today_served):
        self.number_served += today_served


restaurant = Restaurant("Olive Garden", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

Restaurant.describe_restaurant(restaurant)
Restaurant.open_restaurant(restaurant)

# 9-2 Three Restaurants

dominoes = Restaurant("Dominoes", "American-Italian", )
mail_garden = Restaurant("Mail Garden", "Korean")
pho88 = Restaurant("Pho 88", "Vietnamese")

Restaurant.describe_restaurant(dominoes)
Restaurant.describe_restaurant(mail_garden)
Restaurant.describe_restaurant(pho88)


# 9-3 Users

class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user's name is {self.first_name} {self.last_name}. They are {self.age} years old and of the "
              f"{self.gender} gender.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Angela", "Moon", 2000, "female")
user2 = User("Liz", "Biz", 22, "female")
user3 = User("Bill", "Dill", 4, "male")
user4 = User("Mike", "Tyke", 777, "male")

print(user1)

User.describe_user(user1)
User.greet_user(user1)
User.describe_user(user2)
User.greet_user(user2)
User.describe_user(user3)
User.greet_user(user3)
User.describe_user(user4)
User.greet_user(user4)

# 9-4 Number Served

restaurant1 = Restaurant("Moonnnnn", "Korean")
print(restaurant1.number_served)
restaurant1.number_served = 500
print(restaurant1.number_served)

restaurant1.set_number_served(1111)
print(restaurant1.number_served)

restaurant1.increment_number_served(200)
print(restaurant1.number_served)

# 9-5 Login Attempts

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)


# 9-6 Ice Cream Stand

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = []

    def ice_cream_flavors(self):
        print(self.flavor)


baskin = IceCreamStand("Baskin Robbins", "Ice Cream")
baskin.flavor = ['vanilla', 'chocolate', 'rocky road', 'cherry']
baskin.ice_cream_flavors()

# 9-7 Admin

"""class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = []
    def show_privileges(self):
        print(self.privileges)

admin1 = Admin("me", "you", "444", "Neutral")
admin1.privileges = ['can delete post', 'can ban user', 'can change settings']

admin1.show_privileges()"""


# 9-8 Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


admin1 = Admin("me", "you", "444", "Neutral")
admin1.privileges.privileges = ['can delete post', 'can ban user', 'can change settings']
admin1.privileges.show_privileges()

# 9-9 Battery Upgrade


