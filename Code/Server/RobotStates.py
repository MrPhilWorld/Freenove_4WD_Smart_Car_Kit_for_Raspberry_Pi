from enum import Enum

class RobotStates(Enum):
    FORWARD = 1
    TURN = 2
    BACKWARD = 3
    PATH_DECISION = 4
    CROSSROAD_DETECTION = 5
    FORWARD_WITHOUT_DETECTION = 6
    WIN = 7