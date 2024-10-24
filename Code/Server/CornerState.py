import time
from RobotStates import RobotStates
from State import State
from maze import INFRARED, PWM

class CornerState(State):
    def __init__(self):
        super().__init__()
        

    def setup(self):
        super().setup()
        print("Setup, current state: " + str(INFRARED.get_state()))
        PWM.setMotorModel(-1000, -1000, -1000, -1000)
        time.sleep(0.1)
        PWM.setMotorModel(0, 0, 0, 0)
        time.sleep(1)
        print("Stopped in CornerState, current state: " + str(INFRARED.get_state()))

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        return RobotStates.CORNER_FOUND