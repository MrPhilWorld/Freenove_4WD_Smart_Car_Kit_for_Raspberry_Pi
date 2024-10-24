from RobotStates import RobotStates
from State import State
from maze import INFRARED, OBSTACLE_DETECTION, PWM


class ForwardState(State):
    def __init__(self):
        super().__init__()
        self.STATE = -1

    def setup(self):
        super().setup()
        self.STATE = -1
        OBSTACLE_DETECTION.start()
        pass

    def exit(self):
        super().exit()
        OBSTACLE_DETECTION.stop()

    def run(self) -> RobotStates:
        if (INFRARED.has_left_turn() or INFRARED.has_right_turn() or INFRARED.has_cross_road()):
            print("Corner found, current state: " + str(INFRARED.get_state()))
            return RobotStates.CORNER_FOUND
        
        self.move()

        if OBSTACLE_DETECTION.found_obstacle():
            return RobotStates.BACKWARD
        
        return RobotStates.FORWARD
        

    def move(self):
        state = INFRARED.get_state()

        if (state != self.STATE):
            self.STATE = state
            duties = INFRARED.DUTIES[state]
            PWM.setMotorModel(duties.topLeft, duties.bottomLeft, duties.topRight, duties.bottomRight)