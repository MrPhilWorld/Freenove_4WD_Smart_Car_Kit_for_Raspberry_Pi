from abc import ABC, abstractmethod

from RobotStates import RobotStates
from maze import ENGINE

class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def setup(self):
        print(self.__class__.__name__)
        ENGINE.stop()

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def run(self) -> RobotStates:
        pass