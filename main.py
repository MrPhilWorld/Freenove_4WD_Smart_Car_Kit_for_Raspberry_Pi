from src.classes.Engine import Engine
from src.classes.LightControl import LightControl
from src.classes.Infrared import Infrared
from src.classes.Memory import Memory
from src.classes.ObstacleDetection import ObstacleDetection
from src.enums.RobotStates import RobotStates
from src.state_machine.StateMachine import *

from freenove.Ultrasonic import Ultrasonic

MEMORY=Memory()
ENGINE=Engine()
ULTRASONIC=Ultrasonic()
LIGHT_CONTROL=LightControl()
INFRARED=Infrared()
OBSTACLE_DETECTION=ObstacleDetection()

def run(): 
    state_machine = StateMachine(RobotStates.FORWARD)
    
    try:
        while True:
            state_machine.run()

    except KeyboardInterrupt:
        state_machine.reset()
        print ("\nEnd of program")

# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    run()