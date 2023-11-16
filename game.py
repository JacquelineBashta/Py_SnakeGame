import turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard

import globals as g


class Game:
    def __init__(self) -> None:
        # create Main screen
        self.screen = turtle.Screen()
        # deactivate instant animation, until next self.screen.update()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.setup(width=g.SCREEN_WIDTH, height=g.SCREEN_HEIGHT)
        self.screen.title("Snake Game")

        # create snake object and food object
        self.snake = Snake()
        self.food = Food()
        self.score_board = ScoreBoard()

        self.screen.update()

    def _is_collision(self, a, b, coll_distance):
        return (abs(a.xcor() - b.xcor()) < coll_distance and
                abs(a.ycor() - b.ycor()) < coll_distance)

    def _handle_wall_collision(self):
        snake_head = self.snake.body[0]
        if abs(g.SCREEN_WIDTH/2 - abs(snake_head.xcor())) < g.STEP_SIZE:
            snake_head.setx(snake_head.xcor()*-1)
        elif abs(g.SCREEN_HEIGHT/2 - abs(snake_head.ycor())) < g.STEP_SIZE:
            snake_head.sety(snake_head.ycor()*-1)

    def _is_food_collision(self):
        snake_head = self.snake.body[0]
        food = self.food.food
        return self._is_collision(snake_head, food, 20)

    def _is_snake_collision(self):
        snake_head = self.snake.body[0]
        for part in self.snake.body[1:]:
            if self._is_collision(snake_head, part, 5):
                return True
        return False

    def _make_move(self):
        self.snake.forward()
        self.screen.update()

        self._handle_wall_collision()

        if self._is_snake_collision():
            self.score_board.game_over()

        elif self._is_food_collision():
            self.score_board.update_score()

            # make sure that the food will be located in empty spot
            while self._is_food_collision():
                self.food.add_food()
            self.snake.add_body_part()

            self.screen.ontimer(fun=self._make_move,
                                t=self.score_board.get_delay())

        else:
            self.screen.ontimer(fun=self._make_move,
                                t=self.score_board.get_delay())

    def run(self):

        self.screen.onkey(fun=self.snake.left, key="Left")
        self.screen.onkey(fun=self.snake.right, key="Right")
        self.screen.onkey(fun=self.snake.up, key="Up")
        self.screen.onkey(fun=self.snake.down, key="Down")
        self.screen.listen()
        self._make_move()

        self.screen.mainloop()
