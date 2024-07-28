from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,300)
        self.lpadscore = 0
        self.rpadscore = 0
        self.hideturtle()
        self.update_score()
    
    def left_paddle_score(self):
        self.lpadscore+=1
        self.update_score()

    def right_paddle_score(self):
        self.rpadscore+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.lpadscore} : {self.rpadscore}", False, "center", ("Dillenia", 25))
        
