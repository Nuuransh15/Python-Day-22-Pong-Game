from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_STRETCH_WIDTH = 5
PADDLE_STRETCH_LENGTH = 1
PADDLE_SHAPE = "square"
MOVE_DISTANCE = 20
PADDLE_WIDTH = 20 * PADDLE_STRETCH_WIDTH
UPPER_BOUND = 600 / 2 - PADDLE_WIDTH / 2
LOWER_BOUND = -1 * 600 / 2 + PADDLE_WIDTH / 2


class Paddle(Turtle):

    def __init__(self, initial_x_pos, initial_y_pos):
        super().__init__()
        self.penup()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.turtlesize(stretch_wid=PADDLE_STRETCH_WIDTH, stretch_len=PADDLE_STRETCH_LENGTH)
        self.goto(x=initial_x_pos, y=initial_y_pos)

    def move_up(self):
        if self.ycor() < UPPER_BOUND:
            new_y_pos = self.ycor() + MOVE_DISTANCE
            new_x_pos = self.xcor()
            self.goto(x=new_x_pos, y=new_y_pos)

    def move_down(self):
        if self.ycor() > LOWER_BOUND:
            new_y_pos = self.ycor() - MOVE_DISTANCE
            new_x_pos = self.xcor()
            self.goto(x=new_x_pos, y=new_y_pos)
