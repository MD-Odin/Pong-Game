
from turtle import *
from block import *
from Ball import *
from time import *
from scoreboard import *
screensize(600,800)
title("PONG GAME")
bgcolor("black")

lft_paddle= Blocks((-300,0))
rt_paddle=Blocks((300,0))
penup()
tracer(0)

listen()
onkey(rt_paddle.up,"Up")
onkey(rt_paddle.go_down,"Down")
onkey(lft_paddle.up,"w")
onkey(lft_paddle.go_down,"s")
ball=Ball()
score=Scoreboard()

game_on = True

while game_on is True:
    sleep(ball.mov_spd)
    update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:#Top Wall collision
        ball.bounce()
    if ball.distance(rt_paddle)<50 and ball.xcor()>280 or ball.distance(lft_paddle)<50 and ball.xcor()<-280:#Block collision
        ball.bounce_2()
    if ball.xcor()> 290:#bring ball back and increase score of left player
        ball.reset()
        score.increase_l()
    if ball.xcor()<-290:#bring ball back and increase score of right player
        ball.reset()
        score.increase_r()


exitonclick()
