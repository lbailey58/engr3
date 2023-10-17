[Servo](https://github.com/lbailey58/engr3/blob/main/README.md#servo)

[Distance Sensor](https://github.com/lbailey58/engr3/blob/main/README.md#distance-sensor)

[Motor Control](https://github.com/lbailey58/engr3/blob/main/README.md#motor-control)

[Photointerupter](https://github.com/lbailey58/engr3/blob/main/README.md#photointerupter)

[The Hanger](https://github.com/lbailey58/engr3/blob/main/README.md#the-hanger)

[Swing Arm](https://github.com/lbailey58/engr3/blob/main/README.md#swing-arm)

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

![theThing](media/capTouch.gif)

The servo moves back and forth when I touch the different wires
### Wiring
![wiring](media/servo-sweep-circuit.png)

Except, there would be wires on A0 and A1 for capacitive touch

Image credit to [Arduino](https://docs.arduino.cc/learn/electronics/servo-motors)

### Reflection
The assignment was great; it let me learn the ropes of github and Visual Studio code. I also really enjoyed learning about Capacitave touch, which I think to be easier to use than buttons. This assignment was a great intro into working in VS code and helped me get used to all of the processes asociated with it.

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
![gif](media/rgbLed.gif)

The led changes colors when I move the acrylic up and down
### Wiring
![wiring](media/poop.png)

Credit to [Hasan Ahmed](https://www.tinkercad.com/things/5REip7gcB1n)
### Reflection

This assignment was hard for me because it heavily relied on being able to find a good library in order to make it work.
This was not helped by the fact that even when I got a library that should have worked, it did not work because I had my cathode rgb led wired like an anode rgb led.
All of the problems I faced culminated in me being unprogressive for multiple class periods in a row, even though I was trying to be productive.
One thing I learned from this assignment is that the examples on websites with libraries will not always be exaclty what you need, so you need to build a frankenstein of code from multiple differnent websites.

## Motor Control

### Description & Code
We were assigned to control a motor with a potentiometer without using an H-Bridge

```python

#imports
import board
import pwmio
from analogio import AnalogIn

#Setting up the potentiometer
potentiometer = AnalogIn(board.A0)

#Setting up the motor
motor = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=65535)




while True:
    #Makes it so the value doesn't change mid-loop
    a = potentiometer.value

    #sets the motors speed to the potentiometer value
    motor.duty_cycle = a

    #prints the value
    print(a)

```

### Evidence
![gif](media/motorControl.gif)

### Wiring
![Motor Wiring](media/motorWiring.png)

Credit to [Mr. Helmsetter](https://cvilleschools.instructure.com/courses/40347/assignments/544954?module_item_id=1907201)

![Potentiometer](media/potentiometer.png)

Credit to [the Robotics Back-End](https://roboticsbackend.com/arduino-potentiometer-complete-tutorial/)

### Reflection

This assignment was useful for learning how to control a motor in circuitpython.
I was suprised that we did not use H-Bridges and I think that the way that we do it is a bit overcomplicated.
One challenge I ran into along the way was a battery with a negative charge, witch was something I had never seen before.
Overall this assignment was a good way to learn how to learn about new compnents and a good way to learn to control a motor.


## Photointerupter

### Description & Code
Write a description of your assignment first.

```python
#imports
import digitalio
import board
import time

#declaring the photointerupter as an object
pi = digitalio.DigitalInOut(board.D3)

#other variable declares (ignore misspelling)
inerupts = 0
x = False

while True:
    #getting the time since the start of the program
    now = time.monotonic()
    
    #if it's interupted and not bouncing add one to interupts
    if(pi.value and not x):
        inerupts +=1
        x = True

    #Every 4 seconds print the message
    if(now % 4 == 0):
        print("I have been interupted "+ str(inerupts) +" times")
    
    #debouncing
    if(x and not pi.value):
        x = False

```

### Evidence

![gif](media/potentiometer.gif)

### Wiring
![wiring](media/interupterWiring.webp)

Everything is the same as the photo except that we used different photointerupters

Credit to [Arduino Modules](https://arduinomodules.info/ky-010-photo-interrupter-module/)

### Reflection
During this asignment, I learned how to use the time.monotonic function as well as the photointerupter in circuitpython. 
This assignment was also useful for learning the digitalio library. One issue that I ran into was that my photoinerupter wasn't triggering.

## The Hanger

### Description
We were assigned to make a part from a drawing


### Evidence
![part](media\hi.png)
[link](https://cvilleschools.onshape.com/documents/8c427e1606f1d98488399484/w/542500ae5d8a09b11482a609/e/cdeced8ec882bba05865d85d?renderMode=0&uiState=652ed73b2144ae45637caf8f)

### Reflection
This assignment was a good refesher for CAD. 
It warmed me back up after the summer away.
I didn't really learn anything new because the part was pretty simple.

## Swing Arm

### Description
In this assignment, we were told to create a complex part from drawings. We had to use variables in our design to make it so that we could change the part later.

### Evidence

![SwingArm](media/swingArm.png)
[link](https://cvilleschools.onshape.com/documents/62792585bf20051ac83ecd4c/w/260f2a6b03b6cee2875957cb/e/51c002dab6e73429a487b67d?renderMode=0&uiState=652ed78f7160a27eab2d3a30)
### Reflection
This assignment was challenging because of the complexity of the part and the amount of information we were given. This assignment taught me how to make sense of more complex drawings. I had one main error, wich was that I mixed up the sides of the arm (one is long and the other is short)

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

