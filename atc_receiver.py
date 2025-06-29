import random

class ATCReceiver:
    def receive_signal(self):
        signals = [
            "Climb and maintain 10,000 feet",
            "Turn left heading 270",
            "Descend to FL200",
            "Contact tower on 118.7",
            "Maintain current heading",
        ]
        message = random.choice(signals)
        print(f"ATC Message: {message}")
        return message
