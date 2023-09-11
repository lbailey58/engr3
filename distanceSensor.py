import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)
red = 0
green = 0


while True:
    try:
        if(sonar.distance < 20):
            red = 255
            green = (sonar.distance-20)*-12.75
        elif(sonar.distance is 20):
            red = 255
            green = 255
        else:
            green = 255
            red = (sonar.distance-20)*12.75
    except RuntimeError:
        print("Retrying!")
    
    time.sleep(0.1)