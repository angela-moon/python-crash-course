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

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


restaurant = Restaurant("Olive Garden", "Italian")