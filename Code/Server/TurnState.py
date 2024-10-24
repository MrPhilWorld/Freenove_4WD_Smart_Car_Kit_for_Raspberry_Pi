import time
from RobotStates import RobotStates
from State import State
from maze import INFRARED, PWM

class TurnState(State):
    def __init__(self):
        super().__init__()
        self.INITIAL_TIME = time.time()

    def setup(self):
        super().setup()
        self.state = INFRARED.get_state()
        duties = INFRARED.DUTIES[self.state]
        PWM.setMotorModel(duties.topLeft, duties.bottomLeft, duties.topRight, duties.bottomRight)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        state = INFRARED.get_state()

        if (state == 2):
            return RobotStates.FORWARD
        
        return RobotStates.TURN