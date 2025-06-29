from six_pack.airspeed_indicator import AirspeedIndicator
from six_pack.attitude_indicator import AttitudeIndicator
from six_pack.altimeter import Altimeter
from six_pack.vertical_speed_indicator import VerticalSpeedIndicator
from six_pack.turn_coordinator import TurnCoordinator
from six_pack.heading_indicator import HeadingIndicator
from atc_communication.atc_receiver import ATCReceiver
import time
import random

def simulate_flight():
    airspeed = AirspeedIndicator()
    attitude = AttitudeIndicator()
    altimeter = Altimeter()
    vsi = VerticalSpeedIndicator()
    turn_coordinator = TurnCoordinator()
    heading = HeadingIndicator()
    atc = ATCReceiver()

    for _ in range(10):
        speed = random.randint(140, 280)
        pitch = random.uniform(-10, 10)
        roll = random.uniform(-30, 30)
        altitude = random.randint(1000, 40000)
        vs = random.randint(-3000, 3000)
        turn = random.uniform(-2, 2)
        heading_value = random.randint(0, 360)

        airspeed.update(speed)
        attitude.update(pitch, roll)
        altimeter.update(altitude)
        vsi.update(vs)
        turn_coordinator.update(turn)
        heading.update(heading_value)

        airspeed.display()
        attitude.display()
        altimeter.display()
        vsi.display()
        turn_coordinator.display()
        heading.display()

        if _ % 3 == 0:
            atc.receive_signal()

        print("-" * 50)
        time.sleep(1)

if __name__ == "__main__":
    simulate_flight()
