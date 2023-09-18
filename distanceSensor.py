import time
import board
import adafruit_hcsr04
import adafruit_rgbled

cm = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)
red = board.D10
green = board.D11
blue = board.D12
led = adafruit_rgbled.RGBLED(red, green, blue)

while True:
    try:
        cm = sonar.distance
        if(cm < 15 and cm > 5):
            led.color = (255, 0, (cm-5)*25.5)
        elif(cm is 15):
            led.color = (255, 0, 255)
        elif(cm > 25 and cm < 35):
            led.color = (0, (cm-25)*25.5, 255)
        elif(cm < 5):
            led.color = (255, 0, 0)
        elif(cm > 45):
            led.color = (0, 255, 0)
        elif(cm > 15 and cm < 25):
            led.color = ((-1*(cm-20)+5)*25.5, 0, 255)
        elif(cm > 35 and cm < 45):
            led.color = (0, 255, (-1*(cm-40)+5)*25.5)
        elif(cm is 25):
            led.color = (0, 0, 255)
        elif(cm is 35):
            led.color = (0, 255, 255)
    except RuntimeError:
        print("Retrying!")
    print(cm)

    time.sleep(0.1)