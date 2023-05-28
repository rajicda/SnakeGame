from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        move_back = 0
        for _ in range(3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.setx(move_back)
            turtle.speed(1)
            move_back -= 20
            self.segments.append(turtle)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_number - 1].xcor()
            y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x, y)
        self.segments[0].forward(20)
