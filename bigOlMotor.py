import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01
STEPS = 100
#               A1                                  A2                                  B1                              B2        
coils = (digitalio.DigitalInOut(board.D9), digitalio.DigitalInOut(board.D10), digitalio.DigitalInOut(board.D11), digitalio.DigitalInOut(board.D12),)

#setting the coil pins as an output
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

#creating the motor
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

while(True):
    for step in range(STEPS):
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)

    for step in range(STEPS):
        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(DELAY)