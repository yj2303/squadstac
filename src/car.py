class Car(object):
    def __init__(self):
        self._registration_num = None
        self._age = None

    @property
    def registration_num(self):
        return self._registration_num

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @classmethod
    def create(cls, registration_num, age):
        car_obj = cls()
        car_obj.registration_num = registration_num
        car_obj.age = age
        return car_obj
    @registration_num.setter
    def registration_num(self, value):
        self._registration_num = value
