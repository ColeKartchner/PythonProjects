import move
import turtle

def randomwalk(steps):
    turtle.shape("turtle")
    turtle.color("blue")
    for i in range(steps):
        turtle.left(move.angle())
        turtle.forward(10)
    turtle.bye()

if __name__ == "__main__":
    randomwalk(200)
