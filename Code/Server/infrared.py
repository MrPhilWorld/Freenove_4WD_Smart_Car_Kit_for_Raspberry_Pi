from Duties import *

from Line_Tracking import *

INFRARED=Line_Tracking()

class Infrared:
    def __init__(self):
        self.L_SENSOR = GPIO.input(INFRARED.IR01)
        self.M_SENSOR = GPIO.input(INFRARED.IR02)
        self.R_SENSOR = GPIO.input(INFRARED.IR03)
        self.DUTIES = {
            0: Duties(800, 800, 800, 800),
            1: Duties(2500, 2500, -1500, -1500),
            2: Duties(800, 800, 800, 800),
            3: Duties(4000,4000,-2000,-2000),
            4: Duties(-1500,-1500,2500,2500),
            5: Duties(800, 800, 800, 800),
            6: Duties(-2000,-2000,4000,4000),
            7: Duties(4000, 4000, -2000, -2000)
        }
    
    def get_state(self):
        self.L_SENSOR = GPIO.input(INFRARED.IR01)
        self.M_SENSOR = GPIO.input(INFRARED.IR02)
        self.R_SENSOR = GPIO.input(INFRARED.IR03)
        state = 0
        if self.L_SENSOR == True:
            state=(state | 4)
        if self.M_SENSOR == True:
            state=(state | 2)
        if self.R_SENSOR == True:
            state=(state | 1)
        return state
    
    def is_L_activated(self):
        self.L_SENSOR = GPIO.input(INFRARED.IR01)
        return self.L_SENSOR
    
    def is_M_activated(self):
        self.M_SENSOR = GPIO.input(INFRARED.IR02)
        return self.M_SENSOR
    
    def is_R_activated(self):
        self.R_SENSOR = GPIO.input(INFRARED.IR03)
        return self.R_SENSOR
    
    def has_left_turn(self):
        return (self.is_L_activated() == True and 
                self.is_M_activated() == True and 
                self.is_R_activated() == False)

    def has_right_turn(self):
        return (self.is_R_activated() == True and 
                self.is_M_activated() == True and 
                self.is_L_activated() == False)
    
    def has_cross_road(self):
        return (self.is_L_activated() == True and 
                self.is_M_activated() == True and 
                self.is_R_activated() == True)
