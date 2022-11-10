import turtle
from turtle import Turtle
import random

turtle.colormode(255)


class Food(Turtle):

    HEADING = [0, 90, 180, 270]

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(random.choice(self.HEADING))
        self.penup()
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Create new turtle in random arena."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setheading(random.choice(self.HEADING))
        self.goto(random_x, random_y)
