import random
import math
import turtle

def drawpoints(darts):
    # create a window
    window = turtle.Screen()
    drawing= turtle.Turtle()
    
    window.setworldcoordinates(0, 0, 1, 1)
    
    # draw the x axis and y axis
    drawing.up()
    drawing.goto(-1,0)
    drawing.down()
    drawing.goto(1,0)
    
    drawing.up()
    drawing.goto(0,1)
    drawing.down()
    drawing.goto(0,-1)
    
    drawing.up()
    
    for i in range(darts):
        x = random.random()
        y = random.random()
        
        #move the turtle cursor to the (x,y) coordinate
        drawing.goto(x,y)
        
        #demonstration of how to color a circle
        # by drawing blue circles when i is even
        # and red circles when i is odd
        calc = math.sqrt(x**2+y**2)
        
        if calc <= 1:
            drawing.color("blue")
        else:
            drawing.color("red")
            
        drawing.dot()
        
def main():
    num = int(input("Enter the number of points to generate:"))
        
    drawpoints(num)
        
if __name__ == "__main__":
    main()
                    