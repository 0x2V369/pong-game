from turtle import Screen
from score_board import ScoreBoard
from ball import Ball
from paddle import Paddle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import time

LEFT_PADDLE_X_COOR = ((SCREEN_WIDTH / 2) * -0.9)
RIGHT_PADDLE_X_COOR = ((SCREEN_WIDTH / 2) * 0.9)
MAX_SCREEN_HEIGHT = (SCREEN_HEIGHT / 2)
MIN_SCREEN_HEIGHT = (SCREEN_HEIGHT / -2)

game_is_on = True

# Setting up the game screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turns of the turtle animation

score_board = ScoreBoard()
r_paddle = Paddle((RIGHT_PADDLE_X_COOR, 0))
l_paddle = Paddle((LEFT_PADDLE_X_COOR, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_is_on:

    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > (MAX_SCREEN_HEIGHT - 30) or ball.ycor() < (MIN_SCREEN_HEIGHT + 30):
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > RIGHT_PADDLE_X_COOR - 30 and ball.distance(r_paddle) <= 50 \
            or ball.xcor() < LEFT_PADDLE_X_COOR + 30 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()

    # Detect that paddle missed the ball
    if ball.xcor() > (RIGHT_PADDLE_X_COOR + 20):
        score_board.l_point()
        ball.reset_position()
        time.sleep(1)

    if ball.xcor() < LEFT_PADDLE_X_COOR - 30:
        score_board.r_point()
        ball.reset_position()
        time.sleep(1)




screen.exitonclick()
