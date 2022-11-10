from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Display player's actual score."""
        self.clear()
        with open("high_score.txt", mode="r") as data:
            self.write(f"Score: {self.score}   [High score: {data.read()}]", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """Save highest score and reset scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Update player's score."""
        self.score += 1
        self.update_scoreboard()
