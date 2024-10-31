from Crossroad import Crossroad
from Directions import Directions

class Memory:
    def __init__(self):
        self.isBacktracking = False
        self.next_direction = Directions.NONE
        self.crossroads: list[Crossroad] = []

    def add_crossroad(self, crossroad: Crossroad):
        self.crossroads.append(crossroad)