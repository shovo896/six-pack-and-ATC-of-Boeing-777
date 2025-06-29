import random

def generate_flight_data():
    return {
        "speed": random.randint(140, 280),
        "pitch": random.uniform(-10, 10),
        "roll": random.uniform(-30, 30),
        "altitude": random.randint(1000, 40000),
        "vs": random.randint(-3000, 3000),
        "turn": random.uniform(-2, 2),
        "heading": random.randint(0, 360)
    }
