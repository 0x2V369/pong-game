from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.moving_towards = "left"
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Main method to move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def add_new_ball(self):
        self.setheading(180)
        self.goto(0, 0)

    def bounce_y(self):
        """Changes y_coor to inverse when wall hits top/bottom of screen."""
        self.y_move *= -1

    def bounce_x(self):
        """Changes x_coor to inverse when a paddle is hit."""
        self.x_move *= -1
        self.ball_speed *= 0.95  # Increase ball speed

    def reset_position(self):
        """When player misses the ball its direction is changed.
        Ball is also placed back in the middle of the screen.
        """
        self.bounce_x()
        self.ball_speed = 0.1  # Reset ball speed
        self.teleport(0, 0)
