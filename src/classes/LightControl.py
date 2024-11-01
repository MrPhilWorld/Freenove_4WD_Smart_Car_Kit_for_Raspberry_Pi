from src.enums.Colors import Colors, ColorsDict
from freenove.Led import Led

class LightControl:
    def __init__(self):
        self.LED = Led()

    def setColor(self, color: Colors, wait_time = 0):
        self.LED.colorWipe(self.LED.strip, ColorsDict[color], wait_time)