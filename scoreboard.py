from turtle import Turtle
FONT = ('Courier', 17, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT, align=ALIGNMENT)