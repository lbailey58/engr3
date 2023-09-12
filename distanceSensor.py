import time
import board
import adafruit_hcsr04
import pwmio


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)
red = pwmio.PWMOut(board.D10)
green = pwmio.PWMOut(board.D11)
blue = pwmio.PWMOut(board.D12)

while True:
    try:
        if(sonar.distance < 20):
            red.duty_cycle = 65535   
            green.duty_cycle = (sonar.distance-20)*-3276.75
            blue.duty_cycle = 0 
        elif(sonar.distance is 20):
            red.duty_cycle = 65535
            green.duty_cycle = 65535
            blue.duty_cycle = 0
        else:
            green.duty_cycle = 65535
            red.duty_cycle = (sonar.distance-20)*3276.75
            blue.duty_cycle = 0
    except RuntimeError:
        print("Retrying!")
    
    time.sleep(0.1)