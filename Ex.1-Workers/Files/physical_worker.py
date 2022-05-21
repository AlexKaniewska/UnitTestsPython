from Files.all_workers import Worker


class PhysicalWorker(Worker):
    def __init__(self, id, name, surname, age, experience, address, city, strength):
        super().__init__(id, name, surname, age, experience, address, city)
        self._strength = strength

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, record):
        self._strength = record

    def worker_value(self):
        return round(self.experience * self._strength / self.age, 2)
