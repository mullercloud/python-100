from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong 2021")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()


    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect contact with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        ball.x_move *= 1.5
        ball.y_move *= 1.5

    #Detect out of bounds (side walls)
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

        # game_is_on = False
        # print("Game Over")






screen.exitonclick()