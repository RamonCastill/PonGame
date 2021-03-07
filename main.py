from turtle import Screen
from player import Player
from computer_player import DrawMidLine, Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
mid_line = DrawMidLine()
player = Player(350, 0)
computer = Player(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(computer.up, "w")
screen.onkey(computer.down, "s")

# UP = 90
# DOWN = 270
# position = DOWN
i = 4
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # computer.move(position)
    # if computer.ycor() > 250:
    #   position = DOWN
    # if computer.ycor() < -250:
    #    position = UP

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player) < 50 and ball.xcor() > 320 or ball.distance(computer) < 50 and ball.xcor() < -320:
        ball.bounce1()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_my_score()
        i -= 1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_computer_score()
        i -= 1

    if i == 1:
        game_is_on = False
        scoreboard.game_over()



screen.update()

screen.exitonclick()
