from turtle import Turtle

MOVE_DISTANCE = 20
NUMBER_OF_STARTING_SNAKES = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.speed = 0.15
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.create_and_set_segment(position)

    def extend(self):
        self.create_and_set_segment(self.segments[-1].position())

    def create_and_set_segment(self, position):
        turtle = Turtle("square")
        turtle.speed(0)
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segments.append(turtle)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_number - 1].xcor()
            y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def increase_speed(self):
        if len(self.segments) == 7:
            self.speed -= 0.05
        if len(self.segments) == 15:
            self.speed -= 0.03
        if len(self.segments) == 20:
            self.speed -= 0.03

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
