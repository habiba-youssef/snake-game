from turtle import Turtle

FONT = ('Courier', 16, 'normal')
ALIGNMENT = 'center'
FONT2 = ('Courier', 100, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.ht()
        self.penup()
        self.color("white")
        self.sety(270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} || Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0

        self.refresh()
