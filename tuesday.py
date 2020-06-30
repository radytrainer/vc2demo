numberOfValue = int(input("Enter number of value: "))
previousValue = 0
numberOfGreater = 0
for index in range(numberOfValue):
    currentValue = int(input())
    if index > 0 and currentValue > previousValue:
        numberOfGreater = numberOfGreater + 1
        
    previousValue = currentValue

print("Result is: ", numberOfGreater)