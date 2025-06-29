class HeadingIndicator:
    def __init__(self):
        self.heading = 0

    def update(self, heading):
        self.heading = heading

    def display(self):
        print(f"Heading: {self.heading}°")
