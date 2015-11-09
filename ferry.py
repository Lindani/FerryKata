class Car:

    def __init__(self, passengers, color):
        self.passengers = passengers
        self.color = color


class Ferry:

    def __init__(self, people_count, car_count):
        self.people_count = people_count
        self.car_count = car_count

    def board(self):
        if self.people_count <= 10 and self.car_count <= 2:
            return "accepted"
        else:
            return "rejected"
