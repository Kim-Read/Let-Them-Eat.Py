from turtle import *
import time

# Set screen size
setup(400, 300)

# Set background colour - change this to something pretty
bgcolor("black")

# Create a ball - change this to something interesting - ball = pie
ball = Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)

# Create paddle 1
paddle1 = Turtle()
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

# Create paddle 2
paddle2 = Turtle()
paddle2.shape("square")
paddle2.color("purple")
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0



time.sleep(10)
