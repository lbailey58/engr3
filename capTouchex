import time
import board
import touchio
import busio

touch_pad = board.A0  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express


touch = touchio.TouchIn(touch_pad)
count = 0

while True:
    if touch.value:
        count += 1
        print(count)
    time.sleep(0.05)