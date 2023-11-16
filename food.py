import turtle
import random as r

import globals as g


FOOD_COLOR = ["yellow", "blue", "green", "gray"]
FOOD_SHAPE = ["circle", "triangle", "square", "turtle"]


class Food:
    def __init__(self):
        self.food = None
        self.add_food()

    def _choose_random_loc(self, side):
        return r.randint(round(-1*side/2 + g.TOLERANCE),
                         round(side/2 - g.TOLERANCE))

    def add_food(self):
        # choose random location
        pos_x = self._choose_random_loc(g.SCREEN_WIDTH)
        pos_y = self._choose_random_loc(g.SCREEN_HEIGHT)
        if self.food is None:
            # create shape in location
            self.food = turtle.Turtle()
            self.food.penup()

        self.food.shape(r.choice(FOOD_SHAPE))
        self.food.color(r.choice(FOOD_COLOR))
        self.food.goto((pos_x, pos_y))
