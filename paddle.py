from turtle import Turtle
from constants import SCREEN_HEIGHT


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        """
        Move paddle up one position
        """
        if (self.ycor() + 65) < (SCREEN_HEIGHT / 2):
            new_y_cor = self.ycor() + 20
            self.goto((self.xcor(), new_y_cor))

    def move_down(self):
        """
        Move paddle down one position
        """
        if (self.ycor() - 65) > (SCREEN_HEIGHT / -2):
            new_y_cor = self.ycor() - 20
            self.goto((self.xcor(), new_y_cor))
