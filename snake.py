import turtle
import globals as g


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SNAKE_HEAD_COLOR = "brown"
SNAKE_COLOR = "orange"


class Snake:

    def __init__(self):
        self.body = []
        self.add_body_part(head=True)
        self.add_body_part()
        self.add_body_part()
        self.head = self.body[0]

    def add_body_part(self, head=False):
        if head:
            part = turtle.Turtle("circle")
            part.penup()
            part.color(SNAKE_HEAD_COLOR)
        else:
            part = self.body[-1].clone()
            part.color(SNAKE_COLOR)

        self.body.append(part)

    def forward(self):
        for i in range(len(self.body)-1, 0, -1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(g.STEP_SIZE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
