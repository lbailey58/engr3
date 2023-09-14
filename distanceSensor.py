import time
import board
import adafruit_hcsr04
import pwmio
import adafruit_rgbled

cm = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)
red = board.D10
green = board.D11
blue = board.D12
led = adafruit_rgbled.RGBLED(red, blue, green)

while True:
    try:
        cm = sonar.distance
        if(cm < 20 and cm > 5):
            led.color = (255,int((cm-5)*17), 0)
        elif(cm is 20):
            led.color = (255, 255, 0)
        elif(cm > 20 and cm < 35):
            led.color = (int((-(cm-27.5)+7.5)*17), 255, 0)
        elif(cm < 5):
            led.color = (255, 0, 0)
        else:
            led.color = (0, 255, 0)
    except RuntimeError:
        print("Retrying!")
    print(cm)
    time.sleep(0.1)