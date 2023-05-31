from turtle import Turtle

class Puddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        newy = self.ycor() + 50
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 50
        self.goto(self.xcor(), newy)
