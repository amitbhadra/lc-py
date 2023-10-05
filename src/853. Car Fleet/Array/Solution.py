class Car:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed

    # reverse sort
    def __lt__(self, other):
        return self.pos > other.pos

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Cars = []
        for i in range(len(position)):
            Cars.append(Car(position[i], speed[i]))

        Cars.sort()
        res = 0
        prev_car_time = float('-inf') # or 0

        for car in Cars:
            final_time = (target - car.pos) / car.speed
            print(prev_car_time, final_time)
            if final_time > prev_car_time:
                res += 1
                prev_car_time = final_time

        return res
