from turtle import Turtle

FONT = ('Courier', 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.display()
