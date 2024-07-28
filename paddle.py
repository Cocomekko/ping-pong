from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.x = self.y = 0
        self.penup()
        self.shape("square")
        self.shapesize(5, 0.5)
        self.color("white")

    def move_paddle(self,x, y):
        self.x = x
        self.y = y
        self.goto(self.x, self.y)

    def go_up(self):
        y = self.ycor()
        y+=20   
        self.move_paddle(self.x, y) 
    
    def go_down(self):
        y = self.ycor()
        y-=20   
        self.move_paddle(self.x, y) 
