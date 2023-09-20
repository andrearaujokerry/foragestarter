from abc import ABC
from datetime import datetime

from battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = datetime.date.today()


    def needs_service(self):
        print(self.current_date)
