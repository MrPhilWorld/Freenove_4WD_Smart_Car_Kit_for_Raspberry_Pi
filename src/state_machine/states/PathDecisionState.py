import random
from src.enums.Colors import Colors
from src.enums.Directions import Directions
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from main import ENGINE, LIGHT_CONTROL, MEMORY

class PathDecisionState(State):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        super().setup()
        self.crossroad = MEMORY.crossroads[-1]
        LIGHT_CONTROL.setColor(Colors.BLUE)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates: 
        if MEMORY.isBacktracking is True:
            MEMORY.isBacktracking = False

        if len(self.crossroad.directions) <= 0:
            MEMORY.isBacktracking = True
            MEMORY.next_direction = self.crossroad.get_direction_with_offset(Directions.NONE)
            MEMORY.crossroads.pop()
            # Choose path to return to previous crossroad instead
            ENGINE.timeout(0.2)
            if MEMORY.next_direction == Directions.FORWARD:
                return RobotStates.FORWARD_WITHOUT_DETECTION
            else:
                return RobotStates.TURN

        direction = self.choose_random_direction(self.crossroad.directions)
        MEMORY.next_direction = self.crossroad.get_direction_with_offset(direction)
        self.crossroad.currentDirectionOffset = direction
        ENGINE.timeout(0.2)
        if MEMORY.next_direction == Directions.FORWARD:
            return RobotStates.FORWARD_WITHOUT_DETECTION
        else:
            return RobotStates.TURN
    
    def choose_random_direction(self, directions: set[Directions]):
        direction = random.choice(tuple(directions))
        directions.remove(direction)
        return direction