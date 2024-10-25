from Colors import Colors
from RobotStates import RobotStates
from State import State
from Directions import Directions
from maze import INFRARED, LIGHT_CONTROL, OBSTACLE_DETECTION, ENGINE


class ForwardState(State):
    def __init__(self):
        super().__init__()
        self.DIRECTION = Directions.NONE

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.GREEN)
        self.DIRECTION = Directions.NONE
        OBSTACLE_DETECTION.start()
        pass

    def exit(self):
        super().exit()
        OBSTACLE_DETECTION.stop()

    def run(self) -> RobotStates:
        direction = INFRARED.get_direction()
        if (INFRARED.requires_turn(direction)):
            return RobotStates.PATH_DECISION
        
        self.move()

        if OBSTACLE_DETECTION.found_obstacle():
            return RobotStates.BACKWARD
        
        return RobotStates.FORWARD

    def move(self):
        direction = INFRARED.get_direction()

        if (direction != self.DIRECTION):
            self.DIRECTION = direction
            ENGINE.setDirection(direction)