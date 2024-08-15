from turtle import Turtle
import random

BALL_COLOR = "white"
BALL_SIZE = 20
BALL_SHAPE = "circle"
BALL_HEADING = 90
INITIAL_BALL_SPEED = [-1, 1]
STARTING_POS = (0, 0)
TIME_INCREMENT = [0.004, 0.0045, 0.005]
SPEED_MULTIPLIER = 0.95


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.x_move = random.choice(INITIAL_BALL_SPEED)
        self.y_move = random.choice(INITIAL_BALL_SPEED)
        self.move_speed = random.choice(TIME_INCREMENT)

    def move(self):
        ball_x_pos = self.xcor() + self.x_move
        ball_y_pos = self.ycor() + self.y_move
        new_pos = (ball_x_pos, ball_y_pos)
        self.goto(new_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= SPEED_MULTIPLIER

    def reinitialise(self):
        self.move_speed = random.choice(TIME_INCREMENT)
        self.goto(STARTING_POS)
        self.bounce_x()
