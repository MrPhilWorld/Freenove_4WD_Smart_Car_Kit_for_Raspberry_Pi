import time    
from Motor import * 
from ADC import *

PWM=Motor()
adc=Adc()

def test_Motor(): 
    speed = 3000

    try:
        while True:
            left_adr = adc.recvADC(1)
            right_adr = adc.recvADC(0)
            left_speed = round(speed / left_adr)
            right_speed = round(speed / right_adr)

            PWM.setMotorModel(-right_speed, -left_speed, right_speed, left_speed)
            print("Left speed: " + str(left_speed))
            print("Right speed: " + str(right_speed))
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
      
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        test_Motor()
        exit() 
    if sys.argv[1] == 'Motor':
        test_Motor()