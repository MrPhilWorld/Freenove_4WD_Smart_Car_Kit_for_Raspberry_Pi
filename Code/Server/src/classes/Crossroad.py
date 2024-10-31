from src.enums.Directions import Directions

class Crossroad:
    def __init__(self):
        self.directions = set[Directions]()
        self.currentDirectionOffset = Directions.NONE

    def get_direction_with_offset(self, direction: Directions):
        if self.currentDirectionOffset == Directions.NONE:
            return direction
        elif self.currentDirectionOffset == Directions.LEFT_TURN:
            if direction == Directions.FORWARD:
                return Directions.LEFT_TURN
            elif direction == Directions.RIGHT_TURN:
                return Directions.FORWARD
            elif direction == Directions.NONE:
                return Directions.RIGHT_TURN
        elif self.currentDirectionOffset == Directions.RIGHT_TURN:
            if direction == Directions.FORWARD:
                return Directions.RIGHT_TURN
            elif direction == Directions.LEFT_TURN:
                return Directions.FORWARD
            elif direction == Directions.NONE:
                return Directions.LEFT_TURN
        elif self.currentDirectionOffset == Directions.FORWARD:
            if direction == Directions.LEFT_TURN:
                return Directions.RIGHT_TURN
            elif direction == Directions.RIGHT_TURN:
                return Directions.LEFT_TURN
            elif direction == Directions.NONE:
                return Directions.FORWARD
        return direction