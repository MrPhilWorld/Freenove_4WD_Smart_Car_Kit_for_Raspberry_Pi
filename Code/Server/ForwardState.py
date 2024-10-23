from ObstacleDetection import ObstacleDetection
from RobotStates import RobotStates
from State import State
from infrared import Infrared
from Motor import PWM

class ForwardState(State):
    def __init__(self, INFRARED: Infrared, OBSTACLE_DETECTION: ObstacleDetection):
        super().__init__()
        self.INFRARED = INFRARED
        self.OBSTACLE_DETECTION = OBSTACLE_DETECTION
        self.STATE = -1

    def setup(self):
        super().setup()
        self.STATE = -1
        self.OBSTACLE_DETECTION.start()
        pass

    def exit(self):
        super().exit()
        self.OBSTACLE_DETECTION.stop()

    def run(self) -> RobotStates:
        if (self.INFRARED.has_cross_road()):
            return RobotStates.TURN
        
        self.move()

        if self.OBSTACLE_DETECTION.found_obstacle():
            return RobotStates.BACKWARD
        
        return RobotStates.FORWARD
        

    def move(self):
        state = self.INFRARED.get_state()

        if (state != self.STATE):
            self.STATE = state
            duties = self.INFRARED.DUTIES[state]
            PWM.setMotorModel(duties.topLeft, duties.bottomLeft, duties.topRight, duties.bottomRight)