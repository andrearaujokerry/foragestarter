import unittest
from datetime import datetime
from fleet.carfactory import CarFactory


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_battery_should_be_serviced_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
