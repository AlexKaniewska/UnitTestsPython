import time


class Company:
    def __init__(self):
        self.stationID = int(round(time.time() * 1000))
        self.worker_list = []

    def add_worker(self, *args):
        for i in args:
            if hasattr(i, 'iq'):
                i.stationID = self.stationID

            self.worker_list.append(i)

    def delete_worker(self, id):
        for i in self.worker_list:
            if i.id == id:
                self.worker_list.remove(i)

    def filter(self, city):
        newlist = [l for l in self.worker_list if l.city == city]
        return newlist

    def sorted(self, what):
        if what == "experience":
            return sorted(self.worker_list, key=lambda x: x.experience, reverse=True)
        elif what == "age":
            return sorted(self.worker_list, key=lambda x: x.age)
        elif what == "surname":
            return sorted(self.worker_list, key=lambda x: x.surname)
        else:
            return False

    def value(self):
        newlist = []
        for i in self.worker_list:
            newlist.append([i, i.worker_value()])
        return newlist
