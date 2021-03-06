SIQ PE-1 (Backend) Take Home Activity 

Problem Statement
--------------------------------------------------------------------------------------------
We own a parking lot that can hold up to ānā cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.
When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).
The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.
Due to government regulation, the system should provide us with the ability to find out:-
Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
Slot number in which a car with a given vehicle registration plate is parked. 
Slot numbers of all slots where cars of drivers of a particular age are parked.
We interact with the system via a file-based input system, i.e. it should accept a filename as an input. The file referenced by filename will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.

Input--

    Create_parking_lot 6
    Park KA-01-HH-1234 driver_age 21
    Park PB-01-HH-1234 driver_age 21
    Slot_numbers_for_driver_of_age 21
    Park PB-01-TG-2341 driver_age 40
    Slot_number_for_car_with_number PB-01-HH-1234
    Leave 2
    Park HR-29-TG-3098 driver_age 39
    Vehicle_registration_number_for_driver_of_age 18

Solution to Parking Lot  problem statement:- 

1. Create a parking lot with 6 number of slots, and started filling them in increasing order.

2. Whenever one slots get free, we fill the rest of the slot also in increasig order. 



For running parking lot design on your local terminal. Follow these steps: 

  1. Download/git clone the repo
  2. python src/main.py

