from fleet.sternman_engine import SternmanEngine
from fleet.capulet_engine import CapuletEngine
from fleet.willoughby_engine import WilloughbyEngine
from fleet.nubbin import NubbinBattery
from fleet.spindler import SpindlerBattery
from car import Car

"""Using the builder design pattern, we will create a "CarFactory" that makes car objects"""


class CarFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on),
                   SpindlerBattery(last_service_date, current_date))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date))
