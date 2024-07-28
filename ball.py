from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = 5
        self.speed(0)
    
    def set_ball(self):
        angle = random.choice([random.randint(-75,75),random.randint(105,255)])
        self.setheading(angle)
    
    def change_direction(self):
        angle = self.heading() + 180 + 180 - 2*self.heading()
        self.setheading(angle) 

    def move_ball(self):
        self.forward(self.ball_speed)

    def increase_ball_speed(self):
        if self.ball_speed<12:
            self.ball_speed+=0.2

    def reset(self):
        self.goto(0,0)
        self.ball_speed = 5
        self.setheading(self.heading()+180)