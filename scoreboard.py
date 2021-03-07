from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.vs_score = 0
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"           {self.vs_score}", align=ALIGNMENT, font=FONT)
        self.write(f"{self.score}             ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_my_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def increase_computer_score(self):
        self.clear()
        self.vs_score += 1
        self.update_score()

