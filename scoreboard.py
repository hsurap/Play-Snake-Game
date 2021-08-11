from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 278)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 8, "normal"))
    def increse_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

