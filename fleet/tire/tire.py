from abc import ABC, abstractmethod

"Represents a tire object"


class Tire(ABC):
    def __init__(self):
        pass

    "Returns true if a tire object needs service, false if not"

    @abstractmethod
    def needs_service(self):
        pass
