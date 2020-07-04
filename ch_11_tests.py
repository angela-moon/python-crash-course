import unittest
from ch_11 import city_country
from ch_11 import Employee

class CCTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country('boston', 'massachusetts', 50000)
        self.assertEqual(formatted_city, 'Boston, Massachusetts - population 50000')

    def setUp(self):
        self.
    def (self):


if __name__ == '__main__':
    unittest.main()
