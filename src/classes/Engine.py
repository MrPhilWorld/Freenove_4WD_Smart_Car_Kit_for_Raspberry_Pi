import time
from src.enums.Directions import Directions
from src.classes.Duties import Duties
from freenove.Motor import Motor

DUTIES = {
    Directions.NONE: Duties(0, 0, 0, 0),
    Directions.FORWARD: Duties(800, 800, 800, 800),
    Directions.BACKWARD: Duties(-800, -800, -800, -800),
    Directions.RIGHT_DEVIATION: Duties(2500, 2500, -2500, -2500),
    Directions.RIGHT_TURN: Duties(4000, 4000, -2000, -2000),
    Directions.LEFT_DEVIATION: Duties(-2500, -2500, 2500, 2500),
    Directions.LEFT_TURN: Duties(-2000, -2000, 4000, 4000),
    Directions.ROTATE: Duties(-4000, -4000, 4000, 4000),
}

class Engine:
    def __init__(self):
        self.PWM=Motor()
        self.current_direction = Directions.NONE

    def setDirection(self, direction: Directions, reverse = False):
        if direction == Directions.IGNORE:
            return
        
        if direction == self.current_direction:
            return

        self.current_direction = direction
        duties = DUTIES[direction]
        if reverse:
            self.PWM.setMotorModel(-duties.topLeft, -duties.bottomLeft, -duties.topRight, -duties.bottomRight)
        else:
            self.PWM.setMotorModel(duties.topLeft, duties.bottomLeft, duties.topRight, duties.bottomRight)

    def setInvertDirection(self, direction: Directions):
        if (direction == Directions.IGNORE):
            return

        self.current_direction = direction
        duties = DUTIES[direction]
        self.PWM.setMotorModel(-duties.topRight, -duties.bottomRight, -duties.topLeft, -duties.bottomLeft)

    def setCustomDirection(self, topLeftDuty: int, bottomLeftDuty: int, topRightDuty: int, bottomRightDuty: int):
        self.current_direction = Directions.CUSTOM
        self.PWM.setMotorModel(topLeftDuty, bottomLeftDuty, topRightDuty, bottomRightDuty)

    def stop(self):
        self.setDirection(Directions.NONE)

    def timeout(self, seconds: int, direction: Directions = Directions.NONE):
        self.setDirection(direction)
        time.sleep(seconds)