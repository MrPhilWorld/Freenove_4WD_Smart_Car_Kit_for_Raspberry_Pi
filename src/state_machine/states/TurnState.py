import time
from src.enums.Colors import Colors
from src.enums.Directions import Directions
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from main import INFRARED, ENGINE, LIGHT_CONTROL, MEMORY

class TurnState(State):
    def __init__(self):
        super().__init__()
        self.ignoreTime = 0.5

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.YELLOW)
        ENGINE.timeout(0.3, Directions.FORWARD)
        self.initialTime = time.time()
        ENGINE.setDirection(MEMORY.next_direction)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        while time.time() - self.initialTime < self.ignoreTime:
            pass

        direction = INFRARED.get_direction()

        if (direction == Directions.FORWARD):
            return RobotStates.FORWARD_WITHOUT_DETECTION
  
        return RobotStates.TURN