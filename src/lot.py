
class ParkingSlot(object):

    def __init__(self, slot_num=None, available=None):
        self.car = None
        self.slot_num = slot_num
        self.available = available

    @property
    def car(self):
        return self._car


    @property
    def slot_num(self):
        return self._slot_num
    @property
    def available(self):
        return self._available


    @car.setter
    def car(self, value):
        self._car = value

    

    @slot_num.setter
    def slot_num(self, value):
        self._slot_num = value

    
    @available.setter
    def available(self, value):
        self._available = value



