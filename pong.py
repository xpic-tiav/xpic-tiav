import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# score
score_1 = 0
score_2 = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = -0

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

start_game = turtle.Turtle()
start_game.speed(0)
start_game.color("white")
start_game.penup()
start_game.hideturtle()
start_game.goto(0, -260)
start_game.write("Press X to start!", align="center", font=("Courier", 24, "normal"))


#funcions
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

def start():
    ball.dy -= 0.4
    ball.dx += 0.4
    start_game.clear()

def game_over():
    pen.clear()
    paddle_a.clear()
    paddle_b.clear()
    ball.clear()

#keyboard biding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(start, "x")

#main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player 1: {score_1}  Player 2: {score_2}", align="center", font=("Courier", 24, "normal"))

    # paddle and ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #game over

    if score_1 == 5:
        game_over()
        gameover1 = turtle.Turtle()
        gameover1.speed(0)
        gameover1.color("white")
        gameover1.penup()
        gameover1.hideturtle()
        gameover1.goto(0, 0)
        gameover1.write("Game Over! Player 1 won!", align="center", font=("Courier", 24, "bold"))

    if score_2 == 5:
        game_over()
        gameover2 = turtle.Turtle()
        gameover2.speed(0)
        gameover2.color("white")
        gameover2.penup()
        gameover2.hideturtle()
        gameover2.goto(0, 0)
        gameover2.write("Game Over! Player 2 won!", align="center", font=("Courier", 24, "bold"))
