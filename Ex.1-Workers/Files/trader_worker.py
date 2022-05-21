from Files.all_workers import Worker


class TraderWorker(Worker):
    def __init__(self, id, name, surname, age, experience, address, city, efficiency, commission):
        super().__init__(id, name, surname, age, experience, address, city)
        self._efficiency = efficiency
        self._commission = commission
        self.low = 60
        self.medium = 90
        self.high = 120

    @property
    def efficiency(self):
        return self._efficiency

    @efficiency.setter
    def efficiency(self, record):
        self._efficiency = record

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, record):
        self._commission = record

    def worker_value(self):
        if self._efficiency == 'LOW':
            return self.low * self.experience
        if self._efficiency == 'MEDIUM':
            return self.medium * self.experience
        elif self._efficiency == 'HIGH':
            return self.high * self.experience
        else:
            return False
