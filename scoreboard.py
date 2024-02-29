from turtle import Turtle
ALIGNS = "center"
FONTS = ("Arial", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNS, font=FONTS)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER!", align = ALIGNS, font = FONTS)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()