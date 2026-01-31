import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
#checks if input is valid
    if radiusOfCircle1 <= 0 and radiusOfCircle2 <= 0:
        return "Error: Radi must be positive numbers"
#calculate area
    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

#finds coverage percentage
    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)
    coverage = (smallerArea / largerArea) * 100

    return coverage