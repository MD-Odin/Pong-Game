from turtle import *


class Blocks(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(4,1)
        self.color("white")
        self.penup()
        self.goto(position)
    def up(self):
        self.penup()
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        self.penup()
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)