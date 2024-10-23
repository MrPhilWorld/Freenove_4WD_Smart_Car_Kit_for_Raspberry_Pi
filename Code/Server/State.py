from abc import ABC, abstractmethod

from RobotStates import RobotStates
from Motor import PWM

class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def setup(self):
        print(self.__class__.__name__)
        PWM.setMotorModel(0, 0, 0, 0)

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def run(self) -> RobotStates:
        pass