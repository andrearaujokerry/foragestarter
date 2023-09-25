import unittest
from datetime import datetime
from fleet.carfactory import CarFactory


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced_palindrome(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced_palindrome(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
