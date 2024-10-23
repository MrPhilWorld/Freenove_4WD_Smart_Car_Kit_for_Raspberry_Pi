from Action import *
from RobotStates import RobotStates
from StateMachine import *

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