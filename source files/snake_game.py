"""
this python file will be the design of a python game
"""
from turtle import Screen
import time
import snake_game_snake_class as snake_class
import snake_game_food_class as food_class
import snake_game_scoreboard_class as scoreboard_class


# import random as rnd

# SNAKE_SIZE = 0
# snake = []
# START_MOVING = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)

game_snake = snake_class.Snake()
game_food = food_class.Food()
game_score = scoreboard_class.Scoreboard()

# game_score.show_score()
game_snake.start_snake()


screen.listen()
screen.onkey(key="Up", fun=game_snake.move_north)
screen.onkey(key="Down", fun=game_snake.move_south)
screen.onkey(key="Left", fun=game_snake.move_west)
screen.onkey(key="Right", fun=game_snake.move_east)
while True:
    time.sleep(0.2)
    game_score.show_score()
    screen.update()
    game_snake.keep_moving_forward()
    if game_snake.game_over is True:
        game_score.show_game_over()
        break
    x_cor = game_snake.snake[0].xcor()
    y_cor = game_snake.snake[0].ycor()

    if game_snake.snake[0].distance(game_food) < 20:
        game_food.rand_location()
        game_snake.make_snake_longer()
        print("nom")
        game_score.increase_score()
    if x_cor > 299 or x_cor < -299 or y_cor > 299 or y_cor < -299:
        print("dead")
        game_score.show_game_over()
        break


screen.exitonclick()
