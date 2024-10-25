import time
from Colors import Colors
from Directions import Directions
from RobotStates import RobotStates
from State import State
from maze import INFRARED, ENGINE, LIGHT_CONTROL

class TurnState(State):
    def __init__(self):
        super().__init__()
        self.ignoreTime = 0.5

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.YELLOW)
        self.initialTime = time.time()
        self.turnDirection = ENGINE.desired_turn_direction
        ENGINE.setDirection(self.turnDirection)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        if (time.time() - self.initialTime < self.ignoreTime):
            return RobotStates.TURN

        direction = INFRARED.get_direction()

        if (direction == Directions.FORWARD):
            return RobotStates.FORWARD

        if (direction != ENGINE.current_direction):
            if (direction != Directions.FORWARD):
                ENGINE.setDirection(direction)
        
        return RobotStates.TURN