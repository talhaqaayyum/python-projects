# Simple Password Generator
# This script generates a strong random password based on user input.

import random
import string

print("Welcome to the Password Generator!")
print("We will create a secure password for you.\n")

# Ask user for password length
while True:
    try:
        length = int(input("How long should your password be? "))
        if length < 4:
            print("Try a longer password for better security.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Define the characters we can use in the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_chars = letters + digits + symbols

# Generate password
password = "".join(random.choice(all_chars) for _ in range(length))

print("\nYour generated password is:")
print(password)
print("\nKeep it safe and don't share it with anyone!")
