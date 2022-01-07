"""
file contains scoreboard class for snake game
"""
from turtle import Turtle


class Scoreboard(Turtle):
    """
    create scoreboard class
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.label_score = "Score: "
        self.label_game_over = "GAME OVER"

    def increase_score(self):
        """
        increase score by 1
        """
        self.score += 1

    def show_score(self):
        """
        show score on screen
        """
        self.clear()
        self.sety(270)
        self.setx(0)
        self.color("white")
        self.penup()
        self.ht()
        self.write(
            (self.label_score + str(self.score)),
            True,
            align="center",
            font=("Arial", 20, "normal"),
        )

    def show_game_over(self):
        """
        show game over on screen
        """
        self.home()
        self.write(
            self.label_game_over, True, align="center", font=("Arial", 30, "normal")
        )
