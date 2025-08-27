import turtle
import winsound

win = turtle.Screen()
win.title("Pong by @KP")
win.setup(width=800, height=600)
win.bgcolor("black")
win.tracer(0)


# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("blue")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_len=1, stretch_wid=5)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("blue")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.goto(0, 0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.dx = 0.1  # dx is nothing but delta x -- represents the small change in x cordinate of ball
ball.dy = -0.1  # dy is nothing but delta y -- represents the small change in y cordinate of ball

# Score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 15, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
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


# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # moves the ball in x dir by 2 pix (i.e, dx pixel)
    ball.sety(ball.ycor() + ball.dy)  # moves the ball in y dir by 2 pix (i.e, dy pixel)

    # Set boundaries
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
   
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 15, "normal"))
        # winsound.PlaySound("pong_game_sound.mp3", winsound.SND_ASYNC)
   
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 15, "normal"))
        # winsound.PlaySound("pong_game_sound.mp3", winsound.SND_ASYNC)

    # Ball and Paddle Collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        # above condition checks, if ball's x cor is greater than 340 pix and less than 350 pix(paddle b is at 350 pix in x dir) - i.e, ball almost touches paddle
        # and if y cor of ball is with in the range of 40 pix up and 40 pix down of paddle's y cor
        ball.setx(340)
        ball.dx *= -1
   
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        # above condition checks, if ball's x cor is less than -340 pix and greater than -350 pix(paddle a is at -350 pix in x dir) - i.e, ball almost touches paddle
        # and if y cor of ball is with in the range of 40 pix up and 40 pix down of paddle's y cor
        ball.setx(-340)
        ball.dx *= -1