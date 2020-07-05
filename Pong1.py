import turtle

wn = turtle.Screen()  # create window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops automatic updating

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
ball.dx = 0.75  # x-axis movement of ball, new attribute
ball.dy = 0.75  # y-axis movement of ball

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

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #  Todo make it so that ball starts from pedal
    if ball.xcor() > 390 :
        ball.goto(0, 0)  # reset ball
        ball.dx *= -1  # reverse direction

    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle ball collision
    # Collision when ball hits certain x coord and y coord of paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)  # set ball to correct position
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)  # set ball to correct position
        ball.dx *= -1

    #  Todo fixed update speed