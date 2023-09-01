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
touch2 = touchio.TouchIn(pin2);

while True:
    if(not(touch1.value is touch2.value)):
        if(touch1.value and angle < 180):
            angle += 0.25
        elif(angle > 0):
            angle -= 0.25
    my_servo.angle = angle
    sleep(0.0025)