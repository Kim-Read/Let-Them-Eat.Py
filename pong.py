from turtle import *
import time

screen = Screen()
screen.title("Pong game")
screen.setup(width=1000 , height=600)

# Create a ball - change this to something interesting - ball = pie
ball = Turtle()
ball.shape("circle")
ball.color("green")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# Create paddle 1
paddle1 = Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

# Create paddle 2
paddle2 = Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("purple")
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

# Game Rules
player1 = 0
player2 = 0

score = Turtle()
score.speed(0)
score.penup()
#Hiding the turtle to show text
score.hideturtle()
#Locating the scoreboard on top of the screen
score.goto(0, 260)
#Showing the score
score.write("Player1 : 0 Player2: 0", align="center", font=("Courier", 20, "bold"))

#def move_pad1_up():

#def move_pad1_down():

#def move_pad2_down():

#def move_pad2_up():

#add keystrokes



mainloop()
