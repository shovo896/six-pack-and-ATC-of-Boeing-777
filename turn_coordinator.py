class TurnCoordinator:
    def __init__(self):
        self.turn_rate = 0

    def update(self, rate):
        self.turn_rate = rate

    def display(self):
        print(f"Turn Rate: {self.turn_rate:.1f}°/s")
