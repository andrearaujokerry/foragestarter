import unittest
from datetime import datetime
from fleet.carfactory import CarFactory


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced_calliope(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,
                                         tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced_calliope(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,
                                         tire_wear)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
