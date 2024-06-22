import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Test Car Park", 100)
        self.entry_sensor = EntrySensor(1, self.car_park, True)
        self.entry_sensor._scan_plate = self.mock_scan_plate_entry

    def mock_scan_plate_entry(self):
        return "FAKE-001"

    def test_detect_vehicle_adds_car(self):
        self.entry_sensor.detect_vehicle()
        self.assertIn("FAKE-001", self.car_park.plates)


class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Test Car Park", 100)
        self.car_park.plates = ["FAKE-004"]
        self.exit_sensor = ExitSensor(1, self.car_park, True)
        self.exit_sensor._scan_plate = self.mock_scan_plate_exit

    def mock_scan_plate_exit(self):
        return "FAKE-004"

    def test_exit_vehicle_removes_car_when_active(self):
        self.exit_sensor.detect_vehicle()
        self.assertNotIn("FAKE-004", self.car_park.plates)


if __name__ == '__main__':
    unittest.main()
