from src.enums.Colors import Colors
from src.enums.Directions import Directions
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from main import LIGHT_CONTROL, ENGINE, INFRARED, MEMORY

class BackwardState(State):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.RED)
        ENGINE.timeout(0.2)
        MEMORY.isBacktracking = True
        ENGINE.timeout(0.3, Directions.ROTATE)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        direction = INFRARED.get_direction()

        if (direction == Directions.FORWARD):
            return RobotStates.FORWARD_WITHOUT_DETECTION

        return RobotStates.BACKWARD