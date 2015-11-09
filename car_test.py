from ferry import Car
from ferry import Ferry
import unittest


class MyTest(unittest.TestCase):
    def test_number_of_passengers(self):
        passenger_number = Car(10, "yellow")

        self.assertEqual(passenger_number.passengers, 10)

    def test_board_method(self):
        passengers = Ferry(10, 2)
        status = passengers.board()

        self.assertEqual(status, "accepted")
if __name__ == '__main__':
    unittest.main()
