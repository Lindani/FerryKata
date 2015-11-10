from ferry import Car
from ferry import Ferry
import unittest


class MyTest(unittest.TestCase):
    def test_number_of_passengers(self):
        car_number = Car(10, "yellow")

        self.assertEqual(car_number.passengers, 10)

    def test_board_method(self):
        # ferry = Ferry(4, 1)
        # car = Car(2, "yellow")
        # status = ferry.board(car)
        # self.assertEqual(status, "accepted")

        # ferry = Ferry(12, 2)
        # car = Car(12, "red")
        # car = Car(2, "blue")
        # status = ferry.board(car)
        ferry = Ferry(20, 4)
        blue_car = Car(12, "blue")
        ferry.board(blue_car)
        self.assertEqual(ferry.car_count, 1)

        red_car = Car(12, "red")
        ferry.board(red_car)

        self.assertEqual(ferry.car_count, 2)
if __name__ == '__main__':
    unittest.main()
