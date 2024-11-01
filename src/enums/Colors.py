from freenove.Led import Color
from enum import Enum

class Colors(Enum):
    NONE = 0,
    RED = 1,
    GREEN = 2,
    BLUE = 3,
    ORANGE = 4,
    YELLOW = 5

ColorsDict: dict[Colors, Color] = {
    Colors.NONE: Color(0, 0, 0),
    Colors.RED: Color(255, 0, 0),
    Colors.GREEN: Color(0, 255, 0),
    Colors.BLUE: Color(0, 0, 255),
    Colors.ORANGE: Color(255, 128, 0),
    Colors.YELLOW: Color(255, 255, 0)
}