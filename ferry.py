class Car:

    def __init__(self, passengers, color):
        self.passengers = passengers
        self.color = color


class Ferry:

    def __init__(self, allowed_people, allowed_cars):
        self.allowed_people = allowed_people
        self.allowed_cars = allowed_cars
        self.car_count = 0
        self.people_count = 0

    def board(self, car):
        # if car.passengers <= self.allowed_people:
        if self.car_count <= self.allowed_cars:

            self.car_count = self.car_count + 1
        # print car.passengers
            return "accepted"
        else:
            return "rejected"
