from RobotStates import RobotStates
from State import State

class BackwardState(State):
    def __init__(self):
        super().__init__()
        

    def setup(self):
        super().setup()

    def exit(self):
        super().exit()

    def run(self) -> RobotStates:
        return RobotStates.BACKWARD