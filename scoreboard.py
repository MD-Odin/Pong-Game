from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore=0
        self.rscore=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.lscore,font=("Courier",20,"normal"))

        self.goto(100, 280)
        self.write(self.rscore,font=("Courier",20,"normal"))


    def increase_l(self):
        self.lscore+=1
        self.update_score()
    def increase_r(self):
        self.rscore+=1
        self.update_score()
