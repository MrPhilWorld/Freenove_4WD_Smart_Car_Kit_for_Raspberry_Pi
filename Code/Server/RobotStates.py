from enum import Enum

class RobotStates(Enum):
    FORWARD = 1
    TURN = 2
    BACKWARD = 3
    CORNER_FOUND = 4