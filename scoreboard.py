from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score_data:
            self.high_score = int(high_score_data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def write_game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.write_score()
