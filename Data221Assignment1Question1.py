threshold = 100#the max value the product should not exceed

#initialize the product and starting number
product = 1
currentNumber = 1

# Loop until the product reaches or exceeds the threshold
for i in range(1, threshold):
    if product < threshold:
        product *= currentNumber
        currentNumber += 1
    else :
        # Stop the loop once the threshold is exceeded
        break
# Output the final results
print('The final product was: ',product)
print('The integer that caused the product to exceed the threshold was  ', currentNumber)

