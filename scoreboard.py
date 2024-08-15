from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WINNING_SCORE = 10
GAME_OVER_TEXT = "GAME OVER!"
COLOR = "white"
MOVE = False
ALIGN = "center"
SCORE_FONT = ("Courier", 60, "bold")
GAME_OVER_FONT = ("Courier", 30, "bold")
LEFT_SCORE_COORD = (-1 * SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 100)
RIGHT_SCORE_COORD = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 100)
GAME_OVER_SPACING = 30


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.color(COLOR)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):

        self.clear()
        self.goto(LEFT_SCORE_COORD)
        self.write(self.l_score, move=MOVE, align=ALIGN, font=SCORE_FONT)

        self.goto(RIGHT_SCORE_COORD)
        self.write(self.r_score, move=MOVE, align=ALIGN, font=SCORE_FONT)

    def game_over(self):
        self.goto(x=0, y=GAME_OVER_SPACING)
        score_text = f"{GAME_OVER_TEXT}"
        self.write(arg=score_text, move=MOVE, align=ALIGN, font=GAME_OVER_FONT)

        self.goto(x=0, y=-1 * GAME_OVER_SPACING)
        if self.r_score >= WINNING_SCORE:
            score_text = "Player 2 (Right) Wins!"
        if self.l_score >= WINNING_SCORE:
            score_text = "Player 1 (Left) Wins!"
        self.write(arg=score_text, move=MOVE, align=ALIGN, font=GAME_OVER_FONT)
