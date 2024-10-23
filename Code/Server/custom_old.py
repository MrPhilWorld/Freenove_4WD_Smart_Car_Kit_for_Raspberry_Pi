import time    
import threading
from Motor import * 
from Ultrasonic import *
from servo import *
from Led import *
from infrared import Infrared
from Action import *

PWM=Motor()
SERVO=Servo() 
ULTRASONIC=Ultrasonic()
LED=Led()
INFRARED=Infrared()

actions: list[Action] = []

previous_action_time = time.time()
is_reversing=False


def set_Next_Action(actions: list[Action], action: Action):
    set_Previous_Action_Time(actions)

    duties = action.duties
    print("Next action " + str(duties.topLeft) + " " + str(duties.bottomLeft) + " " + str(duties.topRight) + " " + str(duties.bottomRight))
    PWM.setMotorModel(duties.topLeft, duties.bottomLeft, duties.topRight, duties.bottomRight)
    actions.append(action)

def set_Previous_Action_Time(actions: list[Action]):
    global previous_action_time

    numActions = len(actions)

    if (numActions > 0):
        actions[len(actions) - 1].duration = time.time() - previous_action_time
    
    previous_action_time = time.time()


def reverse_Actions(actions: list[Action]):
    global previous_action_time
    
    stop_servo_movement()

    set_Previous_Action_Time(actions)

    numActions = len(actions)

    while numActions > 0 and KeyboardInterrupt:
        action = actions.pop()

        reverse_Action(action)
        print("Previous action duration: " + str(action.duration))
        print("numActions: " + str(numActions))
        time.sleep(action.duration)

        numActions = len(actions)

    PWM.setMotorModel(0, 0, 0, 0)
    start_movement()

def reverse_Action(action: Action):
    duties = action.duties
    print("Reversing action " + str(-duties.topLeft) + " " + str(-duties.bottomLeft) + " " + str(-duties.topRight) + " " + str(-duties.bottomRight))
    PWM.setMotorModel(-duties.topLeft, -duties.bottomLeft, -duties.topRight, -duties.bottomRight)

def move_Servo():
    global is_reversing

    try:
        while not is_reversing:
            for i in range(50,130,1):
                SERVO.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(130,50,-1):
                SERVO.setServoPwm('0',i)
                time.sleep(0.01) 
    except KeyboardInterrupt:
        destroy()
        print ("\nEnd of program")

def start_servo_movement():
    global is_reversing
    is_reversing = False
    SERVO.setServoPwm(1, 70)
    servo_thread = threading.Thread(target=move_Servo)
    servo_thread.daemon = True
    servo_thread.start()
    LED.colorWipe(LED.strip, Color(0,255,0), 0)

def stop_servo_movement():
    global is_reversing
    is_reversing = True
    LED.colorWipe(LED.strip, Color(255,0,0), 0)
    
def move(actions: list[Action]):
    state = INFRARED.get_state()

    if (state != INFRARED.PREV_STATE):
        print("------------------")
        print("state: " + str(state))
        print("prev_state: " + str(INFRARED.PREV_STATE))
        action = Action(INFRARED.DUTIES[state])
        if (check_for_intersection(state)):
            ##count_intersections()
            turn()
        else:
            set_Next_Action(actions, action)

def check_for_intersection(state: int):
    return state == 7 or state == 6 or state == 3 or state == 5

def count_intersections():
    global actions

    states: list[int] = []

    state = INFRARED.get_state()
    set_Next_Action(actions, Action(INFRARED.DUTIES[state]))
    path_found = False
    initial_time = time.time()
    maxTime = 2
    while INFRARED.is_M_activated() == False and time.time() - initial_time < maxTime:
        state = INFRARED.get_state()
        if (state != INFRARED.PREV_STATE):
            states.append(state)
            set_Next_Action(actions, Action(INFRARED.DUTIES[state]))

        if (state == 2):
            path_found = True

    print(str(path_found))
    
    paths = 0

    if (path_found == True):
        paths += 1

    if 7 in states:
        paths += 2
    elif 5 in states:
        paths += 2

    print(str(paths))

    while state != current_infrared_state:
        state = INFRARED.get_state()

        if (state != INFRARED.PREV_STATE):
            set_Next_Action(actions, Action(INFRARED.DUTIES[state], True))

def turn():
    global actions

    state = INFRARED.get_state()

    action = Action(INFRARED.DUTIES[state])
    set_Next_Action(actions, action)
    time.sleep(0.5)
    while INFRARED.is_M_activated() == False:
        pass

def obstacle_check():
    distance_detection = 10

    distance = ULTRASONIC.get_distance()
    print(distance)

    if (distance > 0 and distance < distance_detection):
        reverse_Actions(actions)

def run(): 
    global actions
    global current_infrared_state
    
    try:
        start_servo_movement()

        while True:
            move(actions)
            obstacle_check()

    except KeyboardInterrupt:
        destroy()
        print ("\nEnd of program")

def start_movement():
    INFRARED.reset()
    start_servo_movement()

def destroy():
    LED.colorWipe(LED.strip, Color(0,0,0))
    PWM.setMotorModel(0,0,0,0)
    SERVO.setServoPwm('0',90)
    SERVO.setServoPwm('1',90)

# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    run()