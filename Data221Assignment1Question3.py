# Function that computes base raised to the power of exponent
def computePower(baseValue, exponentValue):
    return baseValue ** exponentValue

baseExponentPairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

validPowerResults = []

# Loop through each pair using argument unpacking
for baseValue, exponentValue in baseExponentPairs:

    # Skip pairs with a negative exponent
    if exponentValue < 0:
        continue
    validPowerResults.append(computePower(baseValue, exponentValue))
print(validPowerResults)