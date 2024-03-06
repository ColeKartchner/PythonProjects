import math
import random

x = random.random()
y = random.random()

n=int(input("Enter the number of points to generate:"))
for n in [x, y]: 
     
    if math.sqrt((x)**2+(y)**2) <= 1.0: 
        print(a, "points were within the quarter circle") 
    else:
        print(b, "points were outside the quarter circle")
        