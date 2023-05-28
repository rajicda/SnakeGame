from turtle import Turtle

MOVE_DISTANCE = 20
NUMBER_OF_STARTING_SNAKES = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        move_back = 0
        for _ in range(NUMBER_OF_STARTING_SNAKES):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.setx(move_back)
            move_back -= 20
            self.segments.append(turtle)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_number - 1].xcor()
            y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
