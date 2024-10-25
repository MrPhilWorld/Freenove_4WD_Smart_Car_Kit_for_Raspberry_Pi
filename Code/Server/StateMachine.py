from Colors import Colors
from State import State
from BackwardState import BackwardState
from PathDecisionState import PathDecisionState
from ForwardState import ForwardState
from TurnState import TurnState

from RobotStates import RobotStates
from maze import LIGHT_CONTROL, OBSTACLE_DETECTION, ENGINE

class StateMachine():
    def __init__(self, initial_state: RobotStates = RobotStates.FORWARD):
        self.STATES: dict[RobotStates, State] = { 
            RobotStates.FORWARD: ForwardState(),
            RobotStates.TURN: TurnState(),
            RobotStates.BACKWARD: BackwardState(),
            RobotStates.PATH_DECISION: PathDecisionState()
        }
        self.STATE = initial_state
        self.STATES[self.STATE].setup()

    def run(self):
        next_state = self.STATES[self.STATE].run()

        if (self.STATE != next_state):
            self.STATES[self.STATE].exit()
            self.STATE = next_state
            self.STATES[self.STATE].setup()

    def reset(self):
        LIGHT_CONTROL.setColor(Colors.NONE)
        ENGINE.stop()
        OBSTACLE_DETECTION.reset()