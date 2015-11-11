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
        if self.car_count <= self.allowed_cars\
                and car.passengers <= self.allowed_people:

            self.car_count = self.car_count + 1
            self.people_count = self.people_count + car.passengers
            return "accepted"
        else:
            return "rejected"
