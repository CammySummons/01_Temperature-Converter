# quick component to convert F to degrees C.
# Function takes in value, does conversion and puts answer into a list

def to_c(from_f):
    celcius = (from_f -32) * 5/9
    return celcius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    if ".0" in str(answer):
        ans_statement = "{} degrees F is {:.0f} degrees C".format(item, answer)
        converted.append(ans_statement)
    else:
        ans_statement = "{} degrees F is {:.2f} degrees C".format(item, answer)
        converted.append(ans_statement)

print(converted)
