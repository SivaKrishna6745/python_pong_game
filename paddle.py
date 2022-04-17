from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        # create the paddle
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    # make the paddle move to key stokes
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
