class VerticalSpeedIndicator:
    def __init__(self):
        self.vertical_speed = 0

    def update(self, vs):
        self.vertical_speed = vs

    def display(self):
        print(f"Vertical Speed: {self.vertical_speed} ft/min")
