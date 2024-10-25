import random
import time
from Colors import Colors
from Directions import Directions
from RobotStates import RobotStates
from State import State
from maze import INFRARED, ENGINE, LIGHT_CONTROL

class PathDecisionState(State):
    def __init__(self):
        super().__init__()
        self.stopTime = 0.5
        
    def setup(self):
        self.initialDirection = INFRARED.get_direction()
        self.directionsFound = {self.initialDirection}
        self.initialTime = time.time()
        super().setup()
        LIGHT_CONTROL.setColor(Colors.ORANGE)
        print("PathDecisionState setup, current direction: " + str(self.initialDirection))

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        if (time.time() - self.initialTime < 0.5):
            self.directionsFound.add(INFRARED.get_direction())
            return RobotStates.PATH_DECISION

        if Directions.CROSS_ROAD in self.directionsFound:
            ENGINE.desired_turn_direction = self.choose_random_path()
        else:
            ENGINE.desired_turn_direction = self.initialDirection
            
        print(ENGINE.desired_turn_direction)

        return RobotStates.TURN
    
    def choose_random_path(self):
            print("Choosing random turn")
            randomDirection = random.randint(1, 2)
            if randomDirection == 1:
                return Directions.LEFT_TURN
            else:
                return Directions.RIGHT_TURN