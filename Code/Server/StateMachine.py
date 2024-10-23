from ForwardState import ForwardState
from ObstacleDetection import ObstacleDetection
from RobotStates import RobotStates

from Motor import Motor
from State import State
from TurnState import TurnState
from Ultrasonic import Ultrasonic
from Led import Led, Color
from infrared import Infrared

PWM=Motor()
ULTRASONIC=Ultrasonic()
LED=Led()
INFRARED=Infrared()
OBSTACLE_DETECTION=ObstacleDetection()

class StateMachine():
    def __init__(self, initial_state: RobotStates = RobotStates.FORWARD):
        self.STATES: dict[RobotStates, State] = { 
            RobotStates.FORWARD: ForwardState(INFRARED, OBSTACLE_DETECTION),
            RobotStates.TURN: TurnState(INFRARED)
        }
        self.STATE = initial_state
        self.STATES[self.STATE].setup()

    def run(self):
        next_state = self.STATES[self.STATE].run()

        if (self.STATE != next_state):
            self.STATES[self.STATE].exit()
            self.STATE = next_state
            print(next_state.name)
            self.STATES[self.STATE].setup()

    def reset(self):
        LED.colorWipe(LED.strip, Color(0,0,0))
        PWM.setMotorModel(0,0,0,0)
        OBSTACLE_DETECTION.reset()