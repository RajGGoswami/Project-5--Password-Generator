# Project-5--Password-Generator

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to generate a random, customizable password based on user input.

**Project Overview
**
The Password Generator allows the user to specify:

How many letters

How many symbols

How many numbers

The program then:

Randomly selects characters

Shuffles them for randomness

Outputs a final generated password

**Why this project exists**

This project represents a significant learning milestone where I combined:

Lists

Loops

Randomization

User-driven configuration

It was my first experience generating output that changes every time the program runs.

**What I learned**

How to store and manage collections using lists

How to loop a specific number of times using for loops

How to randomly select values with random.choice()

How to shuffle a list using random.shuffle()

How to combine list elements into a string using join()

How to calculate and verify output length

**How the code works (step-by-step)**

Define lists for letters, numbers, and symbols.

Ask the user how many of each character type they want.

Append random characters to a list based on user input.

Shuffle the list to remove predictable patterns.

Join the list into a single password string.

Print the password

**Example Output**

Welcome to the PyPassword Generator!

How many letters would you like in your password?

5

How many symbols would you like?

5

How many numbers would you like?

5

3Pc$%#310uB+8w&
