from src.enums.Colors import Colors
from states.ForwardWithoutDetectionState import ForwardWithoutDetectionState
from states.PathDecisionState import PathDecisionState
from states.State import State
from states.BackwardState import BackwardState
from states.CrossroadDetectionState import CrossroadDetectionState
from states.ForwardState import ForwardState
from states.TurnState import TurnState
from states.WinState import WinState

from src.enums.RobotStates import RobotStates
from src.maze import LIGHT_CONTROL, OBSTACLE_DETECTION, ENGINE

class StateMachine():
    def __init__(self, initial_state: RobotStates = RobotStates.FORWARD):
        self.STATES: dict[RobotStates, State] = { 
            RobotStates.FORWARD: ForwardState(),
            RobotStates.TURN: TurnState(),
            RobotStates.BACKWARD: BackwardState(),
            RobotStates.CROSSROAD_DETECTION: CrossroadDetectionState(),
            RobotStates.PATH_DECISION: PathDecisionState(),
            RobotStates.FORWARD_WITHOUT_DETECTION: ForwardWithoutDetectionState(),
            RobotStates.WIN: WinState()
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