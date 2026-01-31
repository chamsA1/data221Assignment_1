# Function that creates a nested dictionary from a list of strings
def nestedDictionaryFromStrings(listOfStrings):
    # Dictionary to store the final result
    nestedDictionaryResult = {}

    # Loop through each string in the list
    for currentString in listOfStrings:
        stringLength = len(currentString)

        # Determine if the length is even or odd
        if stringLength % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        # Store the length and parity in a nested dictionary
        nestedDictionaryResult[currentString] = {
            "length": stringLength,
            "parity": parity

        }
    return nestedDictionaryResult

listOfStrings = ['data','science']
NestedDictionaryFromString = nestedDictionaryFromStrings(listOfStrings)
print(NestedDictionaryFromString)

