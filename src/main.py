from display import Display
from car_park import CarPark
from sensor import Sensor, EntrySensor, ExitSensor


# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark("moondalup", 100, "moondalup.txt")


# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(1, car_park, True)


# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(2,car_park, True)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(1, car_park, "Welcome to Moondalup", True)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car in range(10):
    entry_sensor.detect_vehicle()
    print(f"")

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car in range(2):
    exit_sensor.detect_vehicle()

