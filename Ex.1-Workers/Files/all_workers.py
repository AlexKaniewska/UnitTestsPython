from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, id, name, surname, age, experience, address, city):
        self._id = id
        self._name = name
        self._surname = surname
        self._age = age
        self._experience = experience
        self._address = address
        self._city = city

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, record):
        self._id = record

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, record):
        self._name = record

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, record):
        self._surname = record

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, record):
        self._age = record

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, record):
        self._experience = record

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, record):
        self._address = record

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, record):
        self._city = record

    @abstractmethod
    def worker_value(self):
        pass



