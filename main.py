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

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
