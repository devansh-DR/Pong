from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.new_x = 10
        self.new_y = 10
        self.speed_up = 0.1

    def move(self):
        newx = self.xcor() + self.new_x
        newy = self.ycor() + self.new_y
        self.goto(newx, newy)

    def bounce_y(self):
        self.new_y *= -1
        self.speed_up *= 0.9

    def bounce_x(self):
        self.new_x *= -1
        self.speed_up *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.speed_up = 0.1
        self.bounce_x()


