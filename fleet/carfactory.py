from fleet.engine.sternman_engine import SternmanEngine
from fleet.engine.capulet_engine import CapuletEngine
from fleet.engine.willoughby_engine import WilloughbyEngine
from fleet.battery.nubbin import NubbinBattery
from fleet.battery.spindler import SpindlerBattery
from fleet.tire.carrigan import CarriganTire
from fleet.tire.octoprime import OctoprimeTire
from fleet.car import Car

"""Using the builder design pattern, we will create a "CarFactory" that makes car objects"""


class CarFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        return Car(SternmanEngine(warning_light_on),
                   SpindlerBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
                   NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
