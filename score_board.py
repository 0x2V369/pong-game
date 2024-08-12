from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT = ("arial", 30, "normal")
LINE_LENGTH = 25
LINE_BREAK_LENGTH = 15


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.scr_width = SCREEN_WIDTH
        self.scr_height = SCREEN_HEIGHT
        self.update_score()

    def draw_middle_line(self):
        """
        Draws the dashed line in the middle of the game play screen
        """
        y_coor = (self.scr_height / 2) * (-1)
        self.setheading(90)
        self.goto(0, y_coor)
        self.width(4)  # Set the width of the middle line

        while y_coor < ((self.scr_height / 2) * 0.98):
            self.pendown()
            self.forward(LINE_LENGTH)
            self.penup()
            self.forward(LINE_BREAK_LENGTH)
            y_coor += LINE_LENGTH + LINE_BREAK_LENGTH

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        score_height = (SCREEN_HEIGHT / 2) - 50
        self.clear()
        self.draw_middle_line()
        self.goto(-50, score_height)
        self.write(self.l_score, False, "center", font=FONT)
        self.goto(50, score_height)
        self.write(self.r_score, False, "center", font=FONT)
