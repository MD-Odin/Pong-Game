from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.color("white")
        self.x_pos=10
        self.y_pos=10
        self.mov_spd=0.1

    def move(self):
        new_x=self.xcor()+self.x_pos
        new_y=self.ycor()+self.y_pos
        self.goto(new_x,new_y)
    def bounce(self):#Bounce with the top wall and the y_cor decreases after the bounce
        self.y_pos *= -1
    def bounce_2(self):#Bounce with the blocks and x_cor decreases
        self.x_pos *= -1
        self.mov_spd*=0.9

    def reset(self):#bring back the ball to 0,0 and reset the speed of ball
        self.goto(0,0)
        self.mov_spd=0.1
        self.bounce_2()



