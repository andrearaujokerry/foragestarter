from abc import ABC, abstractmethod

"Represents a battery object"


class Battery(ABC):
    def __init__(self):
        pass

    "Returns true if a battery object needs service, false if not"

    @abstractmethod
    def needs_service(self):
        pass
