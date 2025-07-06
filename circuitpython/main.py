import board
import digitalio
import time

# Setup.
red = digitalio.DigitalInOut(board.GP4)
red.direction = digitalio.Direction.OUTPUT
amber = digitalio.DigitalInOut(board.GP3)
amber.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP5)
green.direction = digitalio.Direction.OUTPUT

# Begin by making sure all the LEDs are off.
red.value = False
amber.value = False
green.value = False

while True:
    # Red.
    red.value = True
    time.sleep(3)

    # Red and amber.
    amber.value = True
    time.sleep(1)
    
    # Green.
    red.value = False
    amber.value = False
    green.value = True
    time.sleep(5)

    # Amber.
    green.value = False
    amber.value = True
    time.sleep(2)

    # Amber off (red comes on at top of loop).
    amber.value = False