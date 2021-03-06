import turtle
import os


wn = turtle.Screen()  # create window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops automatic updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Turtle object
paddle_a.speed(0)  # speed of animation to max
paddle_a.shape("square")  # built in shapes
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # change size of rectangle
paddle_a.penup()  # something with lines
paddle_a.goto(-350, 0)  # Navigator

#  Paddle B
paddle_b = turtle.Turtle()  # Turtle object
paddle_b.speed(0)  # speed of animation to max
paddle_b.shape("square")  # built in shapes
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # change size of rectangle
paddle_b.penup()  # something with lines
paddle_b.goto(350, 0)  # Navigator


#  Ball
ball = turtle.Turtle()  # Turtle object
ball.speed(0)  # speed of animation to max
ball.shape("square")  # built in shapes
ball.color("white")
ball.penup()  # something with lines
ball.goto(0, 0)  # Navigator
ball.dx = 0.5  # x-axis movement of ball, new attribute
ball.dy = 0.5  # y-axis movement of ball

# Pen for keeping score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # no drawing line when pen moves
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Game functions


def paddle_a_up():
    # consider taking paddle as input
    # get y coordinate and change it to new value
    y = paddle_a.ycor()  # get y coordinates
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    # Todo consider taking paddle as input
    # Todo way to stop going over top/bottom
    # get y coordinate and change it to new value
    y = paddle_a.ycor()  # get y coordinates
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # listen for input
wn.onkey(paddle_a_up, "w")  # move up on pressing w
wn.onkey(paddle_a_down, "s")

wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

# Main game loop, required for every game, runs constantly
while True:
    wn.update()

    #  Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # account for ball size
        ball.sety(290)  # reset position
        ball.dy *= -1  # reverse direction
        os.system("aplay bounce.wav&")  # & stops delay after playing sound

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    #  Todo make it so that ball starts from pedal
    #  Todo create scoring function to update on hit
    if ball.xcor() > 390:
        ball.goto(0, 0)  # reset ball
        ball.dx *= -1  # reverse direction
        score_a += 1  # score keeping
        pen.clear()  # delete previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle ball collision
    # Collision when ball hits certain x coord and y coord of paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)  # set ball to correct position
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)  # set ball to correct position
        ball.dx *= -1
        os.system("aplay bounce.wav&")


    #  Todo fixed update speed
