left = 0
right = 0
isMove = True
while isMove:
    action = str(input("Action: "))
    if action == "l" or action == "L":
        left = left - 1
    if action == "r" or action == "R":
        right = right + 1
    if action == "s" or action == "S":
        isMove = False
print("The position of Balook is: ", left + right)
