from machine import Pin, ADC
import time

# Toggle swich
toggle_switch = Pin(16, Pin.IN, Pin.PULL_UP)

# ADC pin for soil moisture sensor
soil_moisture = ADC(Pin(28))  # GP26 is ADC0

# Kryptering funktion
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Encrypt only letters
            start = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_message += char  # Keep non-alphabet characters as is
    return encrypted_message

# Dekryptering
def decrypt(message, shift):
    return encrypt(message, -shift)  # Decryption is the reverse of encryption

# Function to get Caesar cipher shift value based on soil moisture
def get_shift():
    value = soil_moisture.read_u16()  # Read ADC value (0-65535)
    shift = int((value / 65535) * 25) + 1  # Scale to a shift between 1 and 26
    print(f"Soil Moisture Value: {value}, Shift: {shift}")
    return shift

# Main loop
while True:
    message = input("Enter a message: ")
    shift = get_shift()  # Get shift value based on soil moisture

    if toggle_switch.value() == 0:  # Switch is pressed (LOW) -> Encrypt
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    else:  # Switch is not pressed (HIGH) -> Decrypt
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    
    time.sleep(1)  # Delay to prevent rapid polling

