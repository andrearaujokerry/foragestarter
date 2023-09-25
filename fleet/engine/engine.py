from abc import ABC, abstractmethod

"Represents an fleet object"


class Engine(ABC):
    def __init__(self):
        pass

    "Returns true if an fleet object needs service, false if not"

    @abstractmethod
    def needs_service(self):
        pass
