# PYTHON CRASH COURSE
# Chapter 9: Classes

from ch_9_classes import Restaurant, User, Admin, Privileges

# 9-1 Restaurant

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

admin1 = Admin("me", "you", "444", "Neutral")
admin1.privileges.privileges = ['can delete post', 'can ban user', 'can change settings']
admin1.privileges.show_privileges()

# 9-9 Battery Upgrade
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            distance = 140
        elif self.battery_size == 85:
            distance = 185

        message = "This car can go approximately " + str(distance)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        self.battery_size = 100


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

car1 = ElectricCar("Toyota", "Sienna", 2011)

car1.battery.get_range()
car1.battery.upgrade_battery()

car1.battery.describe_battery()

# 9-10 Imported Restaurant
""" done """

# 9-11 Imported Admin
""" done """

# 9-12 Multiple Modules
""" done, not really, but i don't feel like it lol """