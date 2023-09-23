from turtle import *
import time

# Game Rules
player1 = 0
player2 = 0

screen = Screen()
# s_width = 1000  # TODO: Added variables for screen w/h so easier to manipulate
# s_height = 500
screen.title("Pong game")
screen.setup(width=1000, height=500)
screen.bgcolor("Black")         # TODO: Changed background colour
# screen.tracer(0)                # TODO: Work out why this was suggested..
# This is what caused the paddles and balls to disappear. Amended.

# Create a ball - change this to something interesting - ball = pie
ball = Turtle()
ball.shape("circle")
ball.color("green")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball_x_dir = 2      # TODO: This and line 23 changed from ball.dx/ball.dy
ball_y_dir = -2


#  TODO: This code is almost identical.. I'm going to create a paddle class/funct because of the extent of repetition
# Create paddle 1
left_paddle = Turtle()      # TODO: I renamed paddle 1 & 2 to left and right to identify easier in functions
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.setpos(-350, 0)
# left_paddle.pendown()     # TODO: Changed this to stop the paddle drawing a line when moving.
left_paddle.dy = 0          # TODO: What is the point of this?

# Create paddle 2
right_paddle = Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("purple")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.dy = 0  # TODO: What is the point of this also? lol

score = Turtle()
score.speed(0)
score.color("Green")        # TODO: Changed this because of black background
score.penup()
# Hiding the turtle to show text
score.hideturtle()
# Locating the scoreboard on top of the screen
score.goto(0, 260)
# Showing the score
score.write("SCORE", align="center", font=("Arial", 26, "bold"))    # TODO: Changed spelling of centre to center.


# defining left paddle movements    # TODO: There is a better function to be made here once working
def l_paddle_up():                  # TODO: Start of function at bottom
    y = left_paddle.ycor()
    y = y + 90
    left_paddle.sety(y)


def l_paddle_down():
    y = left_paddle.ycor()
    y = y - 90
    left_paddle.sety(y)


# defining right paddle movements
def r_paddle_up():
    y = right_paddle.ycor()
    y = y + 90
    right_paddle.sety(y)


def r_paddle_down():
    y = right_paddle.ycor()
    y = y - 90
    right_paddle.sety(y)


# adding keystrokes
screen.listen()
screen.onkeypress(l_paddle_up, 'w') #TODO: 
screen.onkeypress(l_paddle_down, 's') #TODO: Changed keystroke
screen.onkeypress(r_paddle_up, 'Up')
screen.onkeypress(r_paddle_down, 'Down')

screen.exitonclick()


#   TODO: THIS IS ALL NEW/DIFFERENT CODE


# while True:
#     screen.update()
#     # Ball Motion
#     ball.setx(ball.xcor() + ball_x_dir)
#     ball.sety(ball.ycor() + ball_y_dir)
#     # Ball Border
#     if ball.ycor() > s_height:
#         ball.sety(s_height)
#         ball_y_dir *= -1
#     if ball.ycor() > (-s_height):
#         ball.sety(-s_height)
#         ball_y_dir *= -1
#
#     if ball.xcor() > s_width:
#         ball.goto(0,0)
#         ball_x_dir = ball_x_dir
#         player1 += 1
#         score.clear()
#         score.write(f"Player 1:{player1}   Player 2:{player2}", align='centre', font=("Arial", 26, "bold"))


# def move_paddle(keystroke):
#     if keystroke == onkeypress("Left"):
        # y = pick which paddle
        # y = either + or - the set y direction
        # keep running each paddle through this?
        # run this through a while true loop waiting for input
mainloop()  # TODO: Changed sleep.time to mainloop()
