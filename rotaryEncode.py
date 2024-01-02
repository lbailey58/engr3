import rotaryio
import board
import neopixel
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface

menu = ["stop", "caution", "go"]
last_index = None
menu_index = 0

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
#led = neopixel.NeoPixel(board.NEOPIXEL, 1)
#led.brightness = 0.3
#led[0] = (255, 0, 0)


button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

while True:
    menu_index = enc.position
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    if last_index is None or menu_index is not last_index:
        lcd.set_cursor_pos(1,0)
        lcd.print("          ")
        lcd.set_cursor_pos(1,0)
        lcd.print(menu[menu_index_lcd])
    last_index = menu_index
    menu_index_lcd = menu_index%3
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print(menu[menu_index_lcd])
        button_state = None
