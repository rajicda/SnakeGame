from turtle import Screen
from snake import Snake
import random
import time

game_over = False
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


while not game_over:
    screen.update()
    time.sleep(1)

    snake.move()


screen.exitonclick()
