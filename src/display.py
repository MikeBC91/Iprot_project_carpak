class Display:

    def __init__(self,
                 id,
                 car_park,
                 message = "",
                 in_on = False,
                 ):
        self.id = id
        self.message = message
        self.in_on = in_on
        self.car_park = car_park

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f'{self.id}: Display is {"is on" if self.is_on else "is off"}'

