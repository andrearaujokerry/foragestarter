from abc import ABC, abstractmethod

"""Represents a single serviceable object in Lyft's fleet."""


class Serviceable(ABC):
    def __init__(self):
        pass

    "Returns true if a car object needs service, false if not"
    @abstractmethod
    def needs_service(self):
        pass
