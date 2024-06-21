class CarPark:

    def __init__(self,
                 location,
                 capacity,
                 plates,
                 sensors,
                 display):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.display = display or []
        def __str__(self):
            return f'Welcome to {self.location}car park'