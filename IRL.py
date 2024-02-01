import neopixel
import board
import digitalio
#Imports

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

# Set up the IR Sensor using digital pin 2.
ir_sensor = digitalio.DigitalInOut(board.D2)

# Set the photointerrupter as an input.
ir_sensor.direction = digitalio.Direction.INPUT 
            
# Use the internal pull-up resistor.
ir_sensor.pull = digitalio.Pull.UP

counter = 0
print(counter)
hi = True
# While loop runs the code inside continuously.
while True:
    # If an object is near the IR sensor (sensor is LOW):
    if(ir_sensor.value is False):
        #Set the neopixel's color to RED
        if(counter%2 is 0):
            led[0] = (255, 0 , 0)
        else:
            led[0] = (255, 165, 0)
        if(hi):
            hi = False
            counter = counter + 1
            print(counter)
    # If nothing is near the IR sensor (sensor is HIGH)
    else:
        #Set the neopixel's color to GREEN
        if(counter%2 is 0):
            led[0] = (0, 255 , 0)
        else:
            led[0] = (0, 255, 165)
        hi = True