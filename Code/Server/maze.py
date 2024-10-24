from Action import *
from ObstacleDetection import ObstacleDetection
from RobotStates import RobotStates
from StateMachine import *

from Motor import Motor
from Ultrasonic import Ultrasonic
from Led import Led, Color
from infrared import Infrared

PWM=Motor()
ULTRASONIC=Ultrasonic()
LED=Led()
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