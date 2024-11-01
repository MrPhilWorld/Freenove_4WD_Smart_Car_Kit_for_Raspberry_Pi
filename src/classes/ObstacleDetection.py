import threading
import time
from freenove.Ultrasonic import Ultrasonic
from freenove.Servo import Servo

SERVO=Servo() 
ULTRASONIC=Ultrasonic()

class ObstacleDetection():
    def __init__(self):
        self.ACTIVE = False
        self.DISTANCE = 0

    def start(self):
        self.ACTIVE = True
        self.DISTANCE = 0
        SERVO.setServoPwm(1, 70)
        servo_thread = threading.Thread(target=self.move_Servo)
        servo_thread.daemon = True
        servo_thread.start()
        ultrasonic_thread = threading.Thread(target=self.update_distance_check)
        ultrasonic_thread.daemon = True
        ultrasonic_thread.start()

    def stop(self):
        self.ACTIVE = False
        self.DISTANCE = 0

    def move_Servo(self):
        try:
            while self.ACTIVE:
                for i in range(50,130,1):
                    if not self.ACTIVE:
                        break
                    SERVO.setServoPwm('0',i)
                    time.sleep(0.001)
                for i in range(130,50,-1):
                    if not self.ACTIVE:
                        break
                    SERVO.setServoPwm('0',i)
                    time.sleep(0.001) 
        except KeyboardInterrupt:
            self.reset()
            print ("\nEnd of program")

    def found_obstacle(self):
        distance_detection = 10
        return (self.DISTANCE > 0 and self.DISTANCE < distance_detection)
    
    def update_distance_check(self):
        try:
            while self.ACTIVE:
                self.DISTANCE = ULTRASONIC.get_distance()
        except KeyboardInterrupt:
            print ("\nEnd of program")
            
    def reset(self):
        SERVO.setServoPwm('0',90)
        SERVO.setServoPwm('1',90)