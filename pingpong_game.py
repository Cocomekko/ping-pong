from scorecard import Scorecard
from turtle import Screen
from paddle import Paddle
import time
from ball import Ball

window = Screen()
x,y = 1366, 700
window.setup(1.0, 1.0)
window.bgcolor("black")

window.tracer(0)

pad1 = Paddle()
pad1.move_paddle(640, 0)

pad2 = Paddle()
pad2.move_paddle(-640, 0)

ball = Ball()
ball.set_ball()

score = Scorecard()

def move_ball():
    while True:
        ball.move_ball()
        window.update()
        
        if ball.ycor()>=330 or ball.ycor()<=-330:
            ball.change_direction()
        
        if ball.xcor()>=650:
            score.left_paddle_score()
            ball.reset()
        elif ball.xcor()<=-650:
            score.right_paddle_score()
            ball.reset()
            
        if ball.xcor()<=-630.0 and ball.distance(pad2.pos())<58:
            ball.setheading(180 - ball.heading())
            ball.increase_ball_speed()

        if 630.0<=ball.xcor() and ball.distance(pad1.pos())<58:
            ball.setheading(180 - ball.heading())
            ball.increase_ball_speed()
        
        time.sleep(0.01)

window.listen()
window.onkeypress(move_ball)
window.onkeypress(pad1.go_up,"8")
window.onkeypress(pad1.go_down,"2")
window.onkeypress(pad2.go_up,"w")
window.onkeypress(pad2.go_down,"s")

window.update()
window.exitonclick()
