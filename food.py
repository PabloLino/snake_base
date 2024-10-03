from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('red')
        self.speed("fastest")
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
