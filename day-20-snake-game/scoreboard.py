from turtle import Turtle
#
# SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score = {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))


#TODO use 'write' for score
#TODO use clear after score update
