from turtle import Turtle
import time

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.penup()

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.write(arg=f'Score: {self.current_score} | High Score: {self.highest_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
        if self.current_score > self.highest_score:
            with open("data.txt", mode='w') as data:
                data.write(f'{self.current_score}')
        time.sleep(3)
        self.current_score = 0
