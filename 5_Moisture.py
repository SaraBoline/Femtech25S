from machine import ADC, Pin
import time

# Define ADC pin
soil_moisture = ADC(Pin(28))  # GP26 is ADC0

while True:
    value = soil_moisture.read_u16()  # Read ADC value (0-65535)
    voltage = value * 3.3 / 65535  # Convert to voltage
    print(f"Raw Value: {value}, Voltage: {voltage:.2f}V")
    time.sleep(1)  # Wait 1 second
