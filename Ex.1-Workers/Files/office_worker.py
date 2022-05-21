from Files.all_workers import Worker


class OfficeWorker(Worker):
    def __init__(self, id, name, surname, age, experience, address, city, iq):
        super().__init__(id, name, surname, age, experience, address, city)
        self._iq = iq
        self._stationID = None

    @property
    def iq(self):
        return self._iq

    @iq.setter
    def iq(self, record):
        self._iq = record

    @property
    def stationid(self):
        return self._stationID

    @stationid.setter
    def stationid(self, record):
        self._stationID = record

    def worker_value(self):
        return self.experience * self._iq
