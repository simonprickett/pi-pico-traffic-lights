import machine
import time

# Setup.
red = machine.Pin(4, machine.Pin.OUT)
amber = machine.Pin(3, machine.Pin.OUT)
green = machine.Pin(5, machine.Pin.OUT)

# Begin by making sure all the LEDs are off.
red.low()
amber.low()
green.low()

while True:
    # Red.
    red.high()
    time.sleep(3)

    # Red and amber.
    amber.high()
    time.sleep(1)
    
    # Green.
    red.low()
    amber.low()
    green.high()
    time.sleep(5)

    # Amber.
    green.low()
    amber.high()
    time.sleep(2)

    # Amber off (red comes on at top of loop).
    amber.low()