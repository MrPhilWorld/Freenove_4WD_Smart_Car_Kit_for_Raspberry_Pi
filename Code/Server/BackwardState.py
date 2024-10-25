from Colors import Colors
from RobotStates import RobotStates
from State import State
from maze import LIGHT_CONTROL

class BackwardState(State):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.RED)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        return RobotStates.BACKWARD