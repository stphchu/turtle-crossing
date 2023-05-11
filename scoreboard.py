from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.setpos(x=-280, y=250)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", font=FONT, align="center")
