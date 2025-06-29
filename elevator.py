class Elevator:
    def __init__(self):
        self.angle = 0

    def set_angle(self, angle):
        self.angle = angle
        print(f"Elevator angle set to: {angle}°")
