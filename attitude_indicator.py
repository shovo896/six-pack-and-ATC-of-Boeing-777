class AttitudeIndicator:
    def __init__(self):
        self.pitch = 0
        self.roll = 0

    def update(self, pitch, roll):
        self.pitch = pitch
        self.roll = roll

    def display(self):
        print(f"Attitude - Pitch: {self.pitch:.1f}°, Roll: {self.roll:.1f}°")
