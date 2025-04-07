from machine import Pin
import time

# Initialize toggle switch with pull-up resistor
toggle_switch = Pin(16, Pin.IN, Pin.PULL_UP)

# Caesar cipher shift (for encryption and decryption)
shift = 3  # You can change the shift value

# Function for encryption
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Encrypt only letters
            start = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_message += char  # Keep non-alphabet characters as is
    return encrypted_message

# Function for decryption
def decrypt(message, shift):
    return encrypt(message, -shift)  # Decryption is the reverse of encryption

# Main loop
while True:
    # Input message from the user
    message = input("Enter a message: ")

    if toggle_switch.value() == 0:  # Switch is pressed (LOW) -> Encrypt
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    else:  # Switch is not pressed (HIGH) -> Decrypt
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)

    time.sleep(0.5)  # Delay to prevent constant printing

