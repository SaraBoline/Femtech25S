# Neopixel with potentiometer
from neopixel import Neopixel
from machine import Pin, ADC
import time

# Initialize NeoPixel strip
pixels = Neopixel(5, 0, 0, "RGB")  # (num_pixels, state_machine, pin, mode)

# Initialize potentiometer (soil moisture sensor)
adc = ADC(Pin(28, mode=Pin.IN))

# Flag to track if the warning has been printed
warning_printed = False  

def map_to_rainbow_color(value):
    """Map ADC value to a color."""
    if value > 0 and value < 20000:
        return (255, 0, 0)  # Red
    elif value > 20001 and value < 30000:
        return (255, 127, 0)  # Orange
    elif value > 30001:
        return (0, 255, 0)  # Green

while True:
    low_res = adc.read_u16()  # Read sensor value
    color = map_to_rainbow_color(int(low_res))  # Get corresponding color

    # Set NeoPixel color
    pixels.set_pixel(0, color)
    pixels.show()

    # Print values
    print(low_res)
    print('#%02x%02x%02x' % color)

    # Print "Water your plant!" only once when value drops below 10,000
    if low_res < 10000 and not warning_printed:
        print("Water your plant!")
        warning_printed = True  # Set flag so it doesn't print repeatedly

    # Reset flag when value rises above 10,000
    elif low_res >= 10000:
        warning_printed = False  # Allow message to print again on next drop

    time.sleep_ms(1000)  # Wait 1 second

