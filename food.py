from turtle import Turtle
from random import randint
SHAPE = "circle"
COLOR = "red"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.pen(pendown= False, speed=0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = randint(-270, 270)
        random_y = randint(-260, 270)
        self.goto(random_x, random_y)
