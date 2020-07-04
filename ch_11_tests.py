import unittest
from ch_11 import city_country
from ch_11 import Employee

class CCTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country('boston', 'massachusetts', 50000)
        self.assertEqual(formatted_city, 'Boston, Massachusetts - population 50000')

    def setUp(self):
        self.employee1 = Employee("Jim", "Halpert", 90000, "Dunder Mifflin Paper Company")

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 95000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(5000000)
        self.assertEqual(self.employee1.annual_salary, 5090000)


if __name__ == '__main__':
    unittest.main()
