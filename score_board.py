import turtle
import globals as g


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.move_delay = 100
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, g.SCREEN_HEIGHT/2 - g.TOLERANCE)
        self._write_score()

    def _write_score(self):
        self.write(f"Score : {self.score}", align="center",
                   font=("Courier", 14, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self._write_score()
        if self.score % 10 == 0:
            self.move_delay -= 20
            print(f"Speed = {100 - self.move_delay}")

    def get_delay(self):
        return self.move_delay

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center",
                   font=("Courier", 14, "normal"))
