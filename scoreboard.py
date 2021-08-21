from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-240, 250)
        self.hideturtle()
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def inc_score(self):
        self.score += 1
        self.scoreboard_update()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
