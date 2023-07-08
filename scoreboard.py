import turtle
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = 0

        turtle.goto(0, turtle.window_height()/2-30)
        turtle.hideturtle()
        turtle.penup()
        turtle.color("white")
        turtle.write(f'Score: {self.score}', move=False, align="center", font=("Arial", 22, "normal"))

    def add_point(self):
        self.score += 1
        turtle.clear()
        turtle.write(f'Score: {self.score}', move=False, align="center", font=("Arial", 22, "normal"))

    def game_over(self):
        turtle.goto(0, 0)
        turtle.write(f'Game Over!', move=False, align="center", font=("Arial", 22, "normal"))





