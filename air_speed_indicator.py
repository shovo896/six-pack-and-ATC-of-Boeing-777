class AirspeedIndicator:
    def __init__(self):
        self.airspeed = 0

    def update(self, speed):
        self.airspeed = speed

    def display(self):
        print(f"Airspeed: {self.airspeed} knots")
