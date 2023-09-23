from fleet.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        difference = self.current_date - self.last_service_date
        return difference.days > 730
