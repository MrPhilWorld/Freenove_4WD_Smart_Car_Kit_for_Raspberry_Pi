from src.enums.Directions import Directions
import RPi.GPIO as GPIO

DIRECTIONS = {
    0: Directions.IGNORE,
    1: Directions.RIGHT_DEVIATION,
    2: Directions.FORWARD,
    3: Directions.RIGHT_TURN,
    4: Directions.LEFT_DEVIATION,
    5: Directions.IGNORE,
    6: Directions.LEFT_TURN,
    7: Directions.IGNORE
}

class Infrared:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)

        self.L_SENSOR = GPIO.input(self.IR01)
        self.M_SENSOR = GPIO.input(self.IR02)
        self.R_SENSOR = GPIO.input(self.IR03)
    
    def get_direction(self):
        self.L_SENSOR = GPIO.input(self.IR01)
        self.M_SENSOR = GPIO.input(self.IR02)
        self.R_SENSOR = GPIO.input(self.IR03)
        state = 0
        if self.L_SENSOR:
            state=(state | 4)
        if self.M_SENSOR:
            state=(state | 2)
        if self.R_SENSOR:
            state=(state | 1)
        return DIRECTIONS[state]
    
    def requires_turn(self, direction: Directions):
        return direction == Directions.CROSS_ROAD or direction == Directions.LEFT_TURN or direction == Directions.RIGHT_TURN
