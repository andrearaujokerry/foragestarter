from fleet.serviceable import Serviceable
"""Represents a single car in Lyft's fleet. A car has an fleet and a battery Lyft"""


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        super().__init__()
        self.engine = engine
        self.battery = battery
        self.tires = tires

    "Returns true if a car object needs service, false if not"
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
