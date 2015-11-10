from ferry import Car
from ferry import Ferry
import unittest


class MyTest(unittest.TestCase):
    def test_number_of_passengers(self):
        car_number = Car(10, "yellow")

        self.assertEqual(car_number.passengers, 10)

    def test_board_method(self):
        ferry = Ferry(12, 2)

# Passing tests for boarded cars on the ferry
        blue_car = Car(12, "blue")
        ferry.board(blue_car)
        self.assertEqual(ferry.board(blue_car), "accepted")

        brown_car = Car(12, "brown")
        self.assertEqual(ferry.board(brown_car), "accepted")

        white_car = Car(13, "white")
        self.assertEqual(ferry.board(white_car), "rejected")


# Passing test for accepted passengers on the ferry
#         green_car = Car(10, "green")
#         passengers_status = ferry.board(green_car)
#         self.assertEqual(passengers_status, "accepted")


if __name__ == '__main__':
    unittest.main()
