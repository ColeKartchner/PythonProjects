import math

# create the list
number = [3, 2, 7, 8]

# set equation
answer = math.sqrt((number[2] - number[0])**2 + (number[3] - number[1])**2)

#final print
print("The distance between (", number[0], ",", number[1], ") and (", number[2], ",", number[3], ") is", answer)