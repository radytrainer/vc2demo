left = 0
right = 0
down = 0
up = 0
isMove = True
while isMove:
    action = str(input("Action: "))
    if action == "l" or action == "L":
        left = left - 1
    if action == "r" or action == "R":
        right = right + 1
    if action == "u" or action == "U":
        up = up + 1
    if action == "d" or action == "D":
        down = down - 1
    if action == "s" or action == "S":
        isMove = False
print("The position of Balook is: (", left + right , ", ", down + up, ")")
