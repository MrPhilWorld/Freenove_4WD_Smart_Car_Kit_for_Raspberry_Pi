from abc import ABC, abstractmethod

from src.enums.RobotStates import RobotStates

class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def setup(self):
        print(self.__class__.__name__)

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def run(self) -> RobotStates:
        pass