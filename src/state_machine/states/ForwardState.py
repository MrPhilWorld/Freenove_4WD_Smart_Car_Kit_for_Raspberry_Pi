import time
from src.enums.Colors import Colors
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from src.enums.Directions import Directions
from main import INFRARED, LIGHT_CONTROL, MEMORY, OBSTACLE_DETECTION, ENGINE


class ForwardState(State):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        LIGHT_CONTROL.setColor(Colors.GREEN)
        self.lastDirectionDetectedTime = time.time()
        OBSTACLE_DETECTION.start()
        ENGINE.setDirection(Directions.FORWARD)

    def exit(self):
        super().exit()
        OBSTACLE_DETECTION.stop()

    def run(self) -> RobotStates:
        direction = INFRARED.get_direction()
        if (INFRARED.requires_turn(direction)):
            print("requires turn")
            if not MEMORY.isBacktracking:
                MEMORY.next_direction = direction
                return RobotStates.CROSSROAD_DETECTION
            else:
                return RobotStates.PATH_DECISION

        if direction != Directions.IGNORE:
            self.lastDirectionDetectedTime = time.time()

        if time.time() - self.lastDirectionDetectedTime > 1:
            return RobotStates.WIN
        
        self.move()

        if OBSTACLE_DETECTION.found_obstacle():
            return RobotStates.BACKWARD
        
        return RobotStates.FORWARD

    def move(self):
        direction = INFRARED.get_direction()
        ENGINE.setDirection(direction)