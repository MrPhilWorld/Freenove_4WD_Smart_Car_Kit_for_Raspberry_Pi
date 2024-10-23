from dataclasses import dataclass
from Duties import *
@dataclass
class Action:
    def __init__ (
        self, 
        duties: Duties,
        invert: bool = False,
        duration: int = 0
    ):
        if (invert):
            self.duties = Duties(-duties.topLeft, -duties.bottomLeft, -duties.topRight, -duties.bottomRight)
        else:
            self.duties = duties
        self.duration = duration