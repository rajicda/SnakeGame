import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

BOUNDARIES = 295

game_over = False
snake = Snake()
food = Food()
screen = Screen()
scoreboard = ScoreBoard()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

snake.increase_speed()
while not game_over:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
        snake.increase_speed()

    # Detect collision with wall.
    if snake.head.xcor() > BOUNDARIES or snake.head.xcor() < -BOUNDARIES or snake.head.ycor() > BOUNDARIES or \
            snake.head.ycor() < -BOUNDARIES:
        scoreboard.write_game_over()
        game_over = True

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.write_game_over()
            game_over = True


screen.exitonclick()
