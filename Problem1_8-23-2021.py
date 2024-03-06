# Determines the number of elbow bumps in a room with N people
val = int(input("how may people are in the room?"))

bumps = int((val*(val-1))/2)

print("there will be", bumps, "elbow bumps for", val, "people")