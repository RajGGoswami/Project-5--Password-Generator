# Day 5 – Password Generator
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Using lists to store collections of data
# - Looping a specific number of times using for loops
# - Randomly selecting elements from a list
# - Building a list dynamically based on user input
# - Shuffling a list to randomize order
# - Joining a list into a string
#
# This project marks a major step from simple scripts
# to programs that generate non-trivial output dynamically.

import random

# Password Generator Project

# Lists containing all possible characters
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User inputs define password composition
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# List to build the password character by character
password_list = []

# Add random letters
for letter in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for symbol in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for num in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle to ensure randomness in character order
random.shuffle(password_list)

# Convert list of characters into a string
generated_password = ''.join(password_list)

# Output the final password
print(generated_password)

