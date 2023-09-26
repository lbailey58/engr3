import digitalio
import board
import time


pi = digitalio.DigitalInOut(board.D3)

inerupts = 0
x = False

while True:
    now = time.monotonic()
    if(pi.value and not x):
        inerupts +=1
        x = True
    if(now % 4 == 0):
        print("I have been interupted "+ str(inerupts) +" times")
    if(x and not pi.value):
        x = False