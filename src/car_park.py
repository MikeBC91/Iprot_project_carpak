from sensor import Sensor
from display import Display
class CarPark:

    def __init__(self,
                 location,
                 capacity,
                 plates = None,
                 sensors = None,
                 display = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.display = display or []
    def __str__(self):
        return f'Welcome to {self.location} car park'

    def register(self, component):
        """register a component to car park"""
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type!")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.display.append(component)

    def add_car(self, plate):
        self.plates.append(plate)

    def remove_car(self, plate):
        self.plates.remove(plate)

    def update_displays(self):
        for display in self.displays:
            display.update()
            print(f'Updating: {display}')



