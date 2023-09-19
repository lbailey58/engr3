[Servo](https://github.com/lbailey58/engr3/blob/main/README.md#servo)

[Distance Sensor](https://github.com/lbailey58/engr3/blob/main/README.md#distance-sensor)

[COPY THIS](https://github.com/lbailey58/engr3/blob/main/README.md#copy-this)

## Servo

### Description & Code
We were assigned to make a 180° servo sweep back and forth between 180° and 0°, but I
made mine spicy by having the servo be controlled by two capacitave touch wires.

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
from time import sleep
import board
import pwmio
from adafruit_motor import servo
import touchio #imports



# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

pin1 = board.A0 #the pins of the cap touch
pin2 = board.A1
angle = 90 #declaring a variable to store the angle of the servo in


touch1 = touchio.TouchIn(pin1)
touch2 = touchio.TouchIn(pin2) #declaring the cap touch

while True: #starting the loop
    if(not(touch1.value is touch2.value)): #as long as they are not both being touched
        if(touch1.value and angle < 180): #if one of them is being touched write down to move right
            angle += 0.25
        elif(touch2.value and angle > 0):#if the other one of them is being touched write down to move left
            angle -= 0.25
    my_servo.angle = angle #actually move left/right
    sleep(0.0025) #wait a little bit
```

### Evidence

![theThing](media\capTouch.gif)

The servo moves back and forth when I touch the different wires
### Wiring
![wiring](media\servo-sweep-circuit.png)

Except, there would be wires on A0 and A1 for capacitive touch

Image credit to [Arduino](https://docs.arduino.cc/learn/electronics/servo-motors)

### Reflection
The assignment was great; it let me learn the ropes of github and Visual Studio code.

I also really enjoyed learning about Capacitave touch, which I think to be easier to use than buttons.

## Distance Sensor

### Description & Code
We were assigned to use a distance sensor to make the color of a light move through a rainbow\

```python
#imports
import time
import board
import adafruit_hcsr04
import adafruit_rgbled

cm = 0
#starting the distance sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)

#starting the rgb led
red = board.D10
green = board.D11
blue = board.D12
led = adafruit_rgbled.RGBLED(red, green, blue)

while True:
    try: #here in case the sensor hits nothing

        cm = sonar.distance #making it so that cm is a constant

        # (-1*(cm-x)+5) phase out color
        # (cm-x)*25.5 phase in color
        # (red, green, blue)
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

    time.sleep(0.1) #wait a bit

```

### Evidence
![gif](media\rgbLed.gif)

### Wiring
![wiring](media\poop.png)

Credit to [Hasan Ahmed](https://www.tinkercad.com/things/5REip7gcB1n)
### Reflection


## COPY THIS

### Description & Code
Write a description of your assignment first.

```python
Code goes here

```

### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.
Remember you can insert pictures using Markdown or HTML

### Wiring

### Reflection

