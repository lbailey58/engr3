
import time
import board
import pwmio
from analogio import AnalogIn

potentiometer = AnalogIn(board.A0)

motor = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=65535)




while True:
    a = potentiometer.value
    motor.duty_cycle = a
    print(a)
    time.sleep(0.25)       
