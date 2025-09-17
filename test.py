import os
import time

def clear_terminal():
    """
    Clears the terminal screen.
    Works on Windows, macOS, and Linux.
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Example usage:
print("This text will be cleared.")
input("Press Enter to clear the screen...")
clear_terminal()
print("The screen has been cleared!")

time.sleep(1)

clear_terminal()