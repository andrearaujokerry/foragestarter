from abc import ABC, abstractmethod

"Represents a single car in Lyft's fleet. A car has an fleet and a battery Lyft"


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    "Returns true if a car object needs service, false if not"

    @abstractmethod
    def needs_service(self):
        pass
