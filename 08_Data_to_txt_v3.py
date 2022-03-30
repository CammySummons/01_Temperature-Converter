# Source: https://www.guru99.com/reading-and-writing-files-in-python.html
# Includes RegEx to check file name is valid (A-Z a-z 0-9 and underscores)
# Checks if something is valid

import re

# Data to be outputted
data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# Get filename, can't be blank/invalid
# Assume valid data for now
filename = input("Enter a filename (leave off the extension): ")

valid_file = "[A-Zaz]"
if re.match(valid_file, filename):
    # Add .txt suffix
    filename += ".txt"

    # Create file to hold data
    f = open(filename, "w+")

    # Add new line at end of each time
    for item in data:
        f.write(item + "\n")

    # Close file
    f.close()

else:
    print("oops!")
