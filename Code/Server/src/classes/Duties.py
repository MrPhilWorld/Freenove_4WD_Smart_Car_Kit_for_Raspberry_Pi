from dataclasses import dataclass
@dataclass
class Duties:
    def __init__ (
        self, 
        topLeft: int, 
        bottomLeft: int, 
        topRight: int, 
        bottomRight: int,
    ):
        self.topLeft = topLeft
        self.bottomLeft = bottomLeft
        self.topRight = topRight
        self.bottomRight = bottomRight