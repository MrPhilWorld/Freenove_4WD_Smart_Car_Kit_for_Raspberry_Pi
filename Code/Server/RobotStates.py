from enum import Enum

class RobotStates(Enum):
    FORWARD = 1
    TURN = 2
    BACKWARD = 3
    PATH_DECISION = 4