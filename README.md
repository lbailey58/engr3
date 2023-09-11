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
import touchio



# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

pin1 = board.A0
pin2 = board.A1
angle = 90


touch1 = touchio.TouchIn(pin1)
touch2 = touchio.TouchIn(pin2)

while True:
    if(not(touch1.value is touch2.value)):
        if(touch1.value and angle < 180):
            angle += 0.25
        elif(angle > 0):
            angle -= 0.25
    my_servo.angle = angle
    sleep(0.0025)
```

### Evidence

![](media\capTouch.gif)

The servo moves back and forth when I touch the different wires
### Wiring
![](media\servo-sweep-circuit.png)

Except, there would be wires on A0 and A1 for capacitive touch

Image credit to [Arduino](https://docs.arduino.cc/learn/electronics/servo-motors)

### Reflection
The assignment was great; it let me learn the ropes of github and Visual Studio code.

I also really enjoyed learning about Capacitave touch, which I think to be easier to use than buttons.