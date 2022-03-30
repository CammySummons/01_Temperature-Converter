# Source: https://www.guru99.com/reading-and-writing-files-in-python.html

# Need to import the regular expression library re
import re

# data to be outputted
data = ['I', 'love', 'computers']

# Get filename, can't be blank / invalid
# assume valid data for now.

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a Filename (leave off the extension):  ")

    # Has expression to check file name. Can be upper or lower case letters
    valid_char = "[A-Za-z0-9_]"  # Letters or underscores
    for letter in filename:
        if re.match(valid_char, letter):
            continue  # If the letter is valid, goes back and checks the next

        elif letter == " ":  # Otherwise, find problems
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":  # Describe problem
        print(f"Invalid filename - {problem}")
        print()
    else:
        print("You entered a valid filename")  # Or allow valid file name


# add .txt suffix!
filename += ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
