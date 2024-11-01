from src.enums.Colors import Colors
from src.state_machine.states.ForwardWithoutDetectionState import ForwardWithoutDetectionState
from src.state_machine.states.PathDecisionState import PathDecisionState
from src.state_machine.states.State import State
from src.state_machine.states.BackwardState import BackwardState
from src.state_machine.states.CrossroadDetectionState import CrossroadDetectionState
from src.state_machine.states.ForwardState import ForwardState
from src.state_machine.states.TurnState import TurnState
from src.state_machine.states.WinState import WinState

from src.enums.RobotStates import RobotStates
from main import LIGHT_CONTROL, OBSTACLE_DETECTION, ENGINE

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