#Wednesday Two
numberOfValue = int(input("Enter number of value:"))
numberOfSequence = 0
n1 = 0
n2 = 0
if numberOfValue >= 3:
    for index in range(numberOfValue):
        n3 = int(input()) 
        if index >= 2:
            if n2 == n1 + 1 and n3 == n2 + 1:
                numberOfSequence = numberOfSequence + 1
        
        if index >= 1:
            n1 = n2
        n2  = n3 
    print("Number of sequence is: ", numberOfSequence)
else:
    print("This number must be equal to 3 or greater")
