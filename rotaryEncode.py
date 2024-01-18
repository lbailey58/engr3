#importing all of my stuff
import rotaryio
import board
import neopixel
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface

#creating some variables
menu = ["Reds", "Greens", "Blues"]
reds = ["Cancel", "Red", "Orange"]
greens = ["Cancel", "Green", "Mint"]
blues = ["Cancel", "Blue", "Purple"]
last_index = None
menu_index = 0
place = 0

#creating some objects (enc = encoder, lcd = liquid crystal display, led = light emitting diode)
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)

#setting the brightness of the neopixel and the original color of it (red)
led.brightness = 0.3
led[0] = (255, 0, 0)

#setting up the button
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

#THE LOOP
while True:
    #getting where the encoder is
    menu_index = enc.position
    #getting what color the encoder is on
    menu_index_lcd = menu_index%3
    #Writing on the lcd
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    if last_index is None or menu_index is not last_index: #if it's the first time or the knob has been twisted
        #printing stuff out to the lcd
        lcd.set_cursor_pos(1,0)
        lcd.print("          ")
        lcd.set_cursor_pos(1,0)
        if place is 0:
            lcd.print(menu[menu_index_lcd])
        elif place is 1:
            lcd.print(reds[menu_index_lcd])
        elif place is 2:
            lcd.print(greens[menu_index_lcd])
        else:
            lcd.print(blues[menu_index_lcd])
    last_index = menu_index
    if not button.value and button_state is None: #debouncingness
        button_state = "pressed"
    if button.value and button_state == "pressed": #sets the colors
        if place == 0:
            if menu_index_lcd == 0:
                place = 1
            elif menu_index_lcd == 1:
                place = 2
            else:
                place = 3
        elif place == 1:
            if menu_index_lcd == 0:
                place = 0
            elif menu_index_lcd == 1:
                led[0] = (255, 0, 0)
            elif menu_index_lcd == 2:
                led[0] = (255, 43, 89)
        elif place == 2:
            if menu_index_lcd == 0:
                place = 0
            elif menu_index_lcd == 1:
                led[0] = (0, 255, 0)
            else:
                led[0] = (0, 255, 128)
        elif place == 3:
            if menu_index_lcd == 0:
                place = 0
            elif menu_index_lcd == 1:
                led[0] = (0, 0, 255)
            else:
                led[0] = (190, 0, 255)

    button_state = None
