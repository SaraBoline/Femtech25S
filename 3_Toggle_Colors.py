from neopixel import Neopixel
from machine import Pin
import time

#Led light
#num_pixels = 5  # Adjust for your setup
pixels = Neopixel(1, 0, 0, "RGB")  # Ensure correct GRB order

# Initialize toggle switch with pull-up resistor
toggle_switch = Pin(16  , Pin.IN, Pin.PULL_UP)

while True:
    if toggle_switch.value() == 0:  # Switch is pressed (LOW)
        #print("Switch is ON")
        pixels.set_pixel(0, (0, 255, 0))
        pixels.show()
    else:  # Switch is not pressed (HIGH)
        #print("Switch is OFF")
        pixels.set_pixel(0, (255, 0, 0))
        pixels.show()
    
    time.sleep(0.2)  # Delay to prevent constant printingb

