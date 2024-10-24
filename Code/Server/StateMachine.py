from State import State
from BackwardState import BackwardState
from CornerState import CornerState
from ForwardState import ForwardState
from TurnState import TurnState

from RobotStates import RobotStates
from maze import LED, OBSTACLE_DETECTION, PWM, Color

class StateMachine():
    def __init__(self, initial_state: RobotStates = RobotStates.FORWARD):
        self.STATES: dict[RobotStates, State] = { 
            RobotStates.FORWARD: ForwardState(),
            RobotStates.TURN: TurnState(),
            RobotStates.BACKWARD: BackwardState(),
            RobotStates.CORNER_FOUND: CornerState()
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