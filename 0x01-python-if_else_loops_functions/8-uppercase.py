#!/usr/bin/python3

def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ord() and chr()
            char = chr(ord(char) - ord('a') + ord('A'))
        # Print the character without a newline
        print("{:s}".format(char), end='')
    # Print a newline after the loop
    print()
