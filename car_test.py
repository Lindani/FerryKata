from ferry import Car
from ferry import Ferry
import unittest


class MyTest(unittest.TestCase):
    def test_number_of_passengers(self):
        car_passengers = Car(10, "yellow")  # Setup

        self.assertEqual(car_passengers.passengers, 10)  # Test

    def test_board_method_accepted(self):

        ferry = Ferry(20, 2)  # Setup

        blue_car = Car(2, "blue")  # Setup
        boarding_car = ferry.board(blue_car)  # Execute
        self.assertEqual(boarding_car, "accepted")  # Testing status

        brown_car = Car(12, "brown")  # Setup
        boarding_car = ferry.board(brown_car)  # Execute
        self.assertEqual(boarding_car, "accepted")  # Testing status

    def test_board_method_rejected(self):

        ferry = Ferry(20, 2)  # Setup

        white_car = Car(26, "white")  # Setup
        boarding_car = ferry.board(white_car)  # Execute
        self.assertEqual(boarding_car, "rejected")  # Testing status

    def test_board_people_count(self):

        ferry = Ferry(20, 2)  # Setup

        white_car = Car(6, "white")  # Setup
        ferry.board(white_car)  # Execute
        self.assertEqual(ferry.people_count, 6)  # Testing boarding passengers

        red_car = Car(6, "red")  # Setup
        ferry.board(red_car)  # Execute
        self.assertEqual(ferry.people_count, 12)  # Testing boarding passengers

    def test_board_method_car_count(self):

        ferry = Ferry(20, 2)  # Setup

        yellow_car = Car(6, "white")  # Setup
        ferry.board(yellow_car)  # Execute
        self.assertEqual(ferry.car_count, 1)  # Testing boarding cars

        red_car = Car(6, "red")
        ferry.board(red_car)
        self.assertEqual(ferry.car_count, 2)  # Testing boarding cars

        red_car = Car(6, "red")  # Setup
        ferry.board(red_car)  # Execute
        self.assertEqual(ferry.car_count, 3)  # Testing boarding cars


if __name__ == '__main__':
    unittest.main()
