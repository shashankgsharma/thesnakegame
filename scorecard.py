import turtle
ALIGNMENT = "center"
FONT = ("Oxygen", 15, "bold")


class ScoreCard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0

    def display(self):
        self.hideturtle()
        self.penup()
        self.setpos(0, 250)
        self.write(f"Score = {self.user_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

