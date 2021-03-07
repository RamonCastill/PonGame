from turtle import Turtle
import random

STARTING_POSITIONS = [(380, -60), (380, -40), (380, -20), (380, 0), (380, 20), (380, 40), (380, 60)]
ANGLES = [45, 135, 225, 315]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
STAR_POSITION = (-230, -200)


class DrawMidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.setposition(x=0, y=-250 )
        self.goto(x=0, y=220)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce1(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce1()
