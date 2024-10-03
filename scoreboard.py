from turtle import Turtle
import time
import os
import sys

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_score = 0
        self.load_high_score()
        self.penup()

    def load_high_score(self):
        if getattr(sys, 'frozen', False):
            # Estamos em um executável
            data_file = os.path.join(sys._MEIPASS, 'data.txt')
        else:
            # Estamos em um ambiente normal
            data_file = 'data.txt'

        with open(data_file) as data:
            self.highest_score = int(data.read())

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        with open(self.get_data_file_path()) as data:
            self.highest_score = int(data.read())
        self.write(arg=f'Score: {self.current_score} | High Score: {self.highest_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
        if self.current_score > self.highest_score:
            with open(self.get_data_file_path(), mode='w') as data:
                data.write(f'{self.current_score}')
        time.sleep(3)
        self.current_score = 0

    def get_data_file_path(self):
        if getattr(sys, 'frozen', False):
            return os.path.join(sys._MEIPASS, 'data.txt')
        return 'data.txt'
