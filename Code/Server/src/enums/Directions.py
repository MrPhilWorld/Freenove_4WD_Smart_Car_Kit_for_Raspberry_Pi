from enum import Enum

class Directions(Enum):
    NONE = 0
    IGNORE = 1
    FORWARD = 2
    BACKWARD = 3
    LEFT_TURN = 4
    RIGHT_TURN = 5
    CROSS_ROAD = 6
    LEFT_DEVIATION = 7
    RIGHT_DEVIATION = 8
    CUSTOM = 9
    ROTATE = 10