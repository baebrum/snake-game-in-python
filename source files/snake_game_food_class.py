"""
this python file defines the food class for the snake class
"""
from turtle import Turtle
import random as rnd


class Food(Turtle):
    """class for food"""

    def __init__(self):
        """initializer for food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.rand_location()
        # self.setposition((rnd.randint(-300, 300), rnd.randint(-300, 300)))

    def rand_location(self):
        """
        set random location of food
        """
        self.setposition((rnd.randint(-270, 270), rnd.randint(-270, 270)))
