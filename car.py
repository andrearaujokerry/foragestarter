from fleet.serviceable import Serviceable
"""Represents a single car in Lyft's fleet. A car has an fleet and a battery Lyft"""


class Car(Serviceable):
    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    "Returns true if a car object needs service, false if not"
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        return False
