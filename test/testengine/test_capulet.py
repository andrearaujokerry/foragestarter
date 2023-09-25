import unittest
from datetime import datetime
from fleet.carfactory import CarFactory


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced_calliope(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage,
                                         tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced_calliope(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage,
                                         tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced_thovex(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage,
                                       tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced_thovex(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage,
                                       tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
