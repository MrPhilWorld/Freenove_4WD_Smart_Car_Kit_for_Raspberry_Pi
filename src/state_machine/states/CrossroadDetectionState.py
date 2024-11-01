import time
from src.enums.Colors import Colors
from src.classes.Crossroad import Crossroad
from src.enums.Directions import Directions
from src.enums.RobotStates import RobotStates
from src.state_machine.states.State import State
from main import INFRARED, ENGINE, LIGHT_CONTROL, MEMORY

class CrossroadDetectionState(State):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        super().setup()
        self.directionsFound = set()
        self.directionsFound.add(MEMORY.next_direction)
        LIGHT_CONTROL.setColor(Colors.ORANGE)

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:  
        ENGINE.setDirection(Directions.FORWARD)
        initialTime = time.time()
        while time.time() - initialTime < 0.1:
            self.directionsFound.add(INFRARED.get_direction())  

        ENGINE.stop()

        crossroad = Crossroad()

        if Directions.CROSS_ROAD in self.directionsFound:
            crossroad.directions.add(Directions.LEFT_TURN)
            crossroad.directions.add(Directions.RIGHT_TURN)

        if Directions.LEFT_TURN in self.directionsFound:
            crossroad.directions.add(Directions.LEFT_TURN)

        if Directions.RIGHT_TURN in self.directionsFound:
            crossroad.directions.add(Directions.RIGHT_TURN)

        ENGINE.setDirection(Directions.FORWARD)
        time.sleep(0.2)
        direction = INFRARED.get_direction()
        startTime = time.time()
        while direction != Directions.FORWARD and time.time() - startTime < 0.5:
            direction = INFRARED.get_direction()
            ENGINE.setDirection(direction)


        if (direction == Directions.FORWARD):
            crossroad.directions.add(Directions.FORWARD)

        ENGINE.timeout(0.2)

        direction = INFRARED.get_direction()
        ENGINE.setDirection(Directions.BACKWARD)
        while not INFRARED.requires_turn(direction):
            direction = INFRARED.get_direction()

        MEMORY.add_crossroad(crossroad)
        return RobotStates.PATH_DECISION