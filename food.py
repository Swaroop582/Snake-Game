from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1.0 ,stretch_wid=1.0)
        self.color("skyblue")
        self.speed("fastest")
        rand_x=random.randint(-280, 280)
        rand_y=random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

