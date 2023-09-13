import time
import board
import adafruit_hcsr04
import pwmio

cm = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)
red = pwmio.PWMOut(board.D10, frequency=5000, duty_cycle=0)
green = pwmio.PWMOut(board.D11, frequency=5000, duty_cycle=0)
blue = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)

while True:
    try:
        cm = sonar.distance
        if(cm < 20 and cm > 5):
            red.duty_cycle = 65535   
            green.duty_cycle = int((cm-5)*4368)
            blue.duty_cycle = 0 
        elif(cm is 20):
            red.duty_cycle = 65535
            green.duty_cycle = 65535
            blue.duty_cycle = 0
        elif(cm > 20 and cm < 35):
            green.duty_cycle = 65535
            red.duty_cycle = int((cm-20)*4368)
            blue.duty_cycle = 0
        elif(cm < 5):
            red.duty_cycle = 65535
            green.duty_cycle = 0
            blue.duty_cycle = 0
        else:
            red.duty_cycle = 0
            green.duty_cycle = 65535
            blue.duty_cycle = 0
    except RuntimeError:
        print("Retrying!")
    print("red: " + str(red.duty_cycle), "green: " + str(green.duty_cycle), "blue: " + str(blue.duty_cycle), )
    print(cm)
    time.sleep(0.1)