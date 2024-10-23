import threading
import time
from Ultrasonic import Ultrasonic
from servo import Servo

SERVO=Servo() 
ULTRASONIC=Ultrasonic()

class ObstacleDetection():
    def __init__(self):
        self.ACTIVE = False

    def start(self):
        self.ACTIVE = True
        SERVO.setServoPwm(1, 70)
        servo_thread = threading.Thread(target=self.move_Servo)
        servo_thread.daemon = True
        servo_thread.start()

    def stop(self):
        self.ACTIVE = False

    def move_Servo(self):
        try:
            while self.ACTIVE:
                for i in range(50,130,1):
                    SERVO.setServoPwm('0',i)
                    time.sleep(0.01)
                for i in range(130,50,-1):
                    SERVO.setServoPwm('0',i)
                    time.sleep(0.01) 
        except KeyboardInterrupt:
            self.destroy()
            print ("\nEnd of program")

    def found_obstacle(self):
        distance_detection = 10
        distance = ULTRASONIC.get_distance()

        return (distance > 0 and distance < distance_detection)
        
    def reset(self):
        SERVO.setServoPwm('0',90)
        SERVO.setServoPwm('1',90)