import math
import random

points=int(input("Enter the number of points to generate:"))

def estimate_pi(points):
    inside = 0
    outside = 0
    for i in range(points):
        x = random.random()
        y = random.random()
        if math.sqrt((x)**2+(y)**2) <= 1.0: 
            inside = inside + 1
        else:
            outside = outside + 1
    pi=((inside)/(points))*4
    return pi

epi = estimate_pi(points)

print ("An estimate of pi is", epi)