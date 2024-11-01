import time
from src.enums.Colors import Colors
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from src.enums.Directions import Directions
from main import INFRARED, LIGHT_CONTROL, ENGINE


class ForwardWithoutDetectionState(State):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        self.ignoreTime = 0.5
        LIGHT_CONTROL.setColor(Colors.NONE)
        ENGINE.setDirection(Directions.FORWARD)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        initialTime = time.time()
        while time.time() - initialTime < self.ignoreTime:
            self.move()

        return RobotStates.FORWARD

    def move(self):
        direction = INFRARED.get_direction()
        ENGINE.setDirection(direction)