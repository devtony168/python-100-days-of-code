from turtle import Turtle

UP = 20
DOWN = -20


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + UP
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() + DOWN
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)