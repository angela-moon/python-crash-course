# PYTHON CRASH COURSE
# Chapter 11: Testing Your Code

# 11-1 City, Country
def city_country(city, country, population):
    formatted_city = f"{city.title()}, {country.title()} - population {population}"
    return formatted_city


# 11-3 Employee
class Employee:
    def __init__(self, first_name, last_name, annual_salary, store):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.store = store

    def give_raise(self, raise_amt=5000):
        self.annual_salary += raise_amt


employee1 = Employee("Jim", "Halpert", 90000, "Dunder Mifflin Paper Company")
employee1.give_raise()
