# https://leetcode.com/discuss/interview-question/object-oriented-design/1775855/Parking-Lot-LLD-or-Is-this-approach-enough-for-interviews-or-Feedback-appreciated

# Requirements:

#     A parking lot has limited number of parking spots available.
#     The parking spot is based on the vehicle size. A small vehicle can be parked in a parking slot meant for big vehicle but not vice versa.
#     The system should be assigning the nearest parking space available which is specific to the vehicle size.
#     System should provide all the current used spots and the vehicle information.
#     System should provide all the current available spots.
#     System should assign a ticket once the vehicle is assigned a spot and mark the ticket as paid once the vehicle exits the spot.

from enum import Enum
from typing import List


class VehicleSize(Enum):
    SMALL = 0
    BIG = 1


class Car:
    def __init__(self, size: VehicleSize):
        self.size = size
        self.parked = False


class ParkingSpot:
    def __init__(self, size: VehicleSize):
        self.car = None
        self.size = size

    def is_available(self) -> bool:
        return bool(self.car)

    def park(self, car: Car) -> bool:
        if not self.is_available():
            return False
        self.car = car
        return True


class ParkingLot:
    def __init__(self, small_spots: int, big_spots: int):
        self.capacity = small_spots + big_spots

        self.small_spots = [ParkingSpot(VehicleSize.SMALL) for _ in range(small_spots)]
        self.big_spots = [ParkingSpot(VehicleSize.BIG) for _ in range(big_spots)]

    def get_available_spots(self) -> List[ParkingSpot]:
        spots = []
        for spot in self.small_spots:
            if spot.is_available():
                spots.append(spots)
        for spot in self.big_spots:
            if spot.is_available():
                spots.append(spots)
        return spots
