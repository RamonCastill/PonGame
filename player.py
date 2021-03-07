from turtle import Turtle

STARTING_POSITIONS = [(-380, -60), (-380, -40), (-380, -20), (-380, 0), (-380, 20), (-380, 40), (-380, 60)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
STAR_POSITION = (-230, -200)


class Player(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x_position, y_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move(self, direction):
        if direction == UP:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        elif direction == DOWN:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


