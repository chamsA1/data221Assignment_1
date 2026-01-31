from random import random

# Generate a list of random values between 0 and 1
randomValuesList = [random() for i in range(20)]

# creates a random threshold value
thresholdValue = random()

# Sort the list in ascending order
randomValuesList.sort()

matchingIndices = []

# Loop through the sorted list with index and value
for index, value in enumerate(randomValuesList):
    if value >= thresholdValue:
        matchingIndices.append(index)

print("Sorted values:", randomValuesList)
print("x = ", thresholdValue)

if matchingIndices:
    print("Matching indices:", matchingIndices)
else:
    print("No matching indices")

    from random import random

