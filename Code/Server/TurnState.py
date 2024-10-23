import time
from RobotStates import RobotStates
from State import State
from infrared import Infrared

class TurnState(State):
    def __init__(self, INFRARED: Infrared):
        super().__init__()
        self.INITIAL_TIME = time.time()
        self.INFRARED = INFRARED

    def setup(self):
        super().setup()

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        if (self.INFRARED.has_cross_road()):
            return RobotStates.TURN
        
        return RobotStates.TURN