import lot, car

class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def Create_parking_lot(self, no_of_slots):
        """This method will create parking lot if not present already with given
        number of slots.
        Input: no_of_slots - Integer Type
        """
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print("Parking Lot already created")
            return

        if no_of_slots > 0:
            for i in range(1, no_of_slots+1):
                temp_slot = lot.ParkingSlot(slot_num=i,
                                    available=True)
                self.slots[i] = temp_slot
            print("Created parking of %s slots" % no_of_slots)
        else:
            print("Number of slots is incorrect.")
        return

    def get_nearest_available_slot(self):
        """Method to find nearest available slot in parking
        """
        available_slots = [x for x in list(self.slots.values()) if x.available]
        if not available_slots:
            return None
        return sorted(available_slots, key=lambda x: x.slot_num)[0]

    def Park(self, registration_num, driver_age, age):
        """Method to park a coming car in nearest available parking
        slot. If not present it will throw message.
        Input: registration_num - String Type
               age - String Type
        """

        if not self._do_primary_checks():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = car.Car.create(registration_num, age)
            available_slot.available = False
            print("Car with vehicle registration number ",registration_num," has been parked at slot number ",available_slot.slot_num)
        else:
            print("Sorry, parking lot is full.")

    def Leave(self, slot_num):
        """Method to empty a parking slot while car is leaving.
        Input: slot_num - Integer Type
        """
        slot_num = int(slot_num)
        if not self._do_primary_checks():
            return

        if slot_num in self.slots:
            pslot = self.slots[slot_num]
            if not pslot.available and pslot.car:
                pslot.car = None
                pslot.available = True
                print("Slot number ",slot_num," is vacated")
                # the car with vehicle registration number",car.registration_num,
                #" left the space, the driver of the car was of age ",car.age)
            else:
                print("No car is present at slot number %s" % slot_num)
        else:
            print("Sorry, slot number does not exist in parking lot.")

    def Status(self):
        """Method to show current status of parking
        """

        if not self._do_primary_checks():
            return

        print("Slot No\tRegistration No\tAge")
        for i in list(self.slots.values()):
            if not i.available and i.car:
                print("%s\t%s\t%s" % (i.slot_num, i.car.registration_num, i.car.age))

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    def Vehicle_registration_number_for_driver_of_age(self, age):
        """Method to find registration numbers of car with given age in
        parking
        Input: age - String Type
        """

        if not self._do_primary_checks():
            return

        registration_nums = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.age == age:
                registration_nums += '%s ' % pslot.car.registration_num

        if registration_nums:
            print(registration_nums[:-1])
        else:
            print("not found")

    def Slot_numbers_for_driver_of_age(self, age):
        """Method to find slot numbers for cars with given age in
        parking.
        Input: age - String Type
        """

        if not self._do_primary_checks():
            return

        slot_nums = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.age == age:
                slot_nums += '%s ' % pslot.slot_num

        if slot_nums:
            print(slot_nums[:-1])
        else:
            print("Not found")

    def Slot_number_for_car_with_number(self, registration_num):
        """Method to find slot numbers in parking with given registration
        number.
        Input: registration_num - String Type
        """

        if not self._do_primary_checks():
            return

        slot_num = ''
        for pslot in list(self.slots.values()):
            if not pslot.available and pslot.car and \
                pslot.car.registration_num == registration_num:
                slot_num = pslot.slot_num
                break

        if slot_num:
            print(slot_num)
        else:
            print("Not found")

