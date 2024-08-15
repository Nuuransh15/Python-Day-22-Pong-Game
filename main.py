from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Define game parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "PONG"
BALL_SIZE = 20
UP_KEY_P1 = "Up"
DOWN_KEY_P1 = "Down"
UP_KEY_P2 = "w"
DOWN_KEY_P2 = "s"
WINNING_SCORE = 10

P1_INITIAL_POS_X = 350
P1_INITIAL_POS_Y = 0

P2_INITIAL_POS_X = -350
P2_INITIAL_POS_Y = 0

PADDLE_COLLISION_DISTANCE = 52

UPPER_WALL = SCREEN_HEIGHT / 2 - BALL_SIZE / 2
LOWER_WALL = -1 * SCREEN_HEIGHT / 2 + BALL_SIZE / 2
LEFT_WALL = -1 * SCREEN_WIDTH / 2 + BALL_SIZE
RIGHT_WALL = SCREEN_WIDTH / 2 - BALL_SIZE

# Set-up screen
screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# Create paddle 1 object (on right of screen)
paddle_1 = Paddle(initial_x_pos=P1_INITIAL_POS_X, initial_y_pos=P1_INITIAL_POS_Y)

# Create paddle 2 object (on right of screen)
paddle_2 = Paddle(initial_x_pos=P2_INITIAL_POS_X, initial_y_pos=P2_INITIAL_POS_Y)

# Create ball object
pong_ball = Ball()

# Create scoreboard object
my_scoreboard = Scoreboard()

# Invoke screen listener to register key presses
screen.listen()
screen.onkeypress(paddle_1.move_up, key=UP_KEY_P1)
screen.onkeypress(paddle_1.move_down, key=DOWN_KEY_P1)
screen.onkeypress(paddle_2.move_up, key=UP_KEY_P2)
screen.onkeypress(paddle_2.move_down, key=DOWN_KEY_P2)


is_game_on = True
while is_game_on:
    screen.update()
    pong_ball.move()
    time.sleep(pong_ball.move_speed)

    if pong_ball.ycor() >= UPPER_WALL or pong_ball.ycor() <= LOWER_WALL:
        pong_ball.bounce_y()

    if ((pong_ball.xcor() == (P1_INITIAL_POS_X - BALL_SIZE))
            and (paddle_1.distance(pong_ball) <= PADDLE_COLLISION_DISTANCE)
            or (pong_ball.xcor() == (P2_INITIAL_POS_X + BALL_SIZE))
            and (paddle_2.distance(pong_ball) <= PADDLE_COLLISION_DISTANCE)):
        pong_ball.bounce_x()

    if pong_ball.xcor() >= RIGHT_WALL:
        pong_ball.reinitialise()
        my_scoreboard.l_point()

    if pong_ball.xcor() <= LEFT_WALL:
        pong_ball.reinitialise()
        my_scoreboard.r_point()

    if my_scoreboard.r_score >= WINNING_SCORE or my_scoreboard.l_score >= WINNING_SCORE:
        is_game_on = False
        my_scoreboard.game_over()

screen.exitonclick()
