import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper
#import the things that need to be imported

#Setting some variables to be used later
DELAY = 0.01
STEPS = 1

#               A1                                  A2                                  B1                              B2        
coils = (digitalio.DigitalInOut(board.D9), digitalio.DigitalInOut(board.D10), digitalio.DigitalInOut(board.D11), digitalio.DigitalInOut(board.D12),)

#setting the coil pins as an output
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

#creating the motor
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

#Spins the motor while other things are not happening
async def run_motor():
    while(True):
        for step in range(STEPS):
            motor.onestep(style=stepper.DOUBLE)
            time.sleep(DELAY)
        await asyncio.sleep(0)

 #moves the motor backward when the limit switch is clicked
async def catch_pin_transitions(pin):
   
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS*100):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)
    
#runs the functions
async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        motor_task = asyncio.create_task(run_motor())
        await asyncio.gather(interrupt_task, motor_task)



#starts everything going
asyncio.run(main())

    