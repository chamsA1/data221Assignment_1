def cumulativePercentage(numbersList):
    resultDict = {}
    totalCount = len(numbersList)

    # Get sorted unique values from the list
    uniqueNumbers = sorted(set(numbersList))

    # Loop through each unique number
    for number in uniqueNumbers:
        # Count how many elements are less than or equal to the current number
        countLessOrEqual = sum(1 for x in numbersList if x <= number)
        # Calculate the percentage
        percentage = (countLessOrEqual / totalCount) * 100
        # Store the result in the dictionary
        resultDict[number] = percentage

    return resultDict

print(cumulativePercentage([1,2,3,4,5,6]))