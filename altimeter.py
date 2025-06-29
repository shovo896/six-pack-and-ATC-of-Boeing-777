class Altimeter:
    def __init__(self):
        self.altitude = 0

    def update(self, altitude):
        self.altitude = altitude

    def display(self):
        print(f"Altitude: {self.altitude} feet")
