import math
import random

num=int(input("Enter the number of points to generate:"))

inside = 0
outside = 0

for i in range(num):
    
    x = random.random()
    y = random.random()
     
    if math.sqrt((x)**2+(y)**2) <= 1.0: 
        inside = inside + 1
    else:
        outside = outside + 1
        
print(inside, "points were within the quarter circle")
print(outside, "points were outside the quarter circle")