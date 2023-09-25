import unittest
from datetime import datetime
from fleet.carfactory import CarFactory


class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0.75, 0.75, 0.75, 0.75]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0.8, 0.8, 0.8, 0.59]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.5, 0.5, 1, 1]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0.6, 1, 0.6, 0.79]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [1, 1, 1, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [1, 1, 0.99, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()