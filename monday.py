numberOfValue = int(input("Enter number of value: "))
indexOf7 = 0
isSevenFound = False
for i in range(numberOfValue):
    number = int(input())
    if number == 7 and not isSevenFound:  # not false == true
        indexOf7 = i
        isSevenFound = True


if isSevenFound == True:       
    print("index is: " , indexOf7)
else:
    print("No 7 entered")
