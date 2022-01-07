"""
this python contains snake class that allows for movement
"""
from turtle import Turtle


class Snake:
    """
    class is global variables and is meant to be created only once
    contains snake list, size, and if the snake is moving
    """

    def __init__(self):
        self.snake_size = 0
        self.snake = []
        self.start_moving = False
        self.game_over = False

    def did_snake_eat_self(self):
        """
        check if head ate anypart of itself
        """
        for idx in range(1, self.get_snake_size()):
            if self.snake[0].position() == self.snake[idx].position():
                self.game_over = True
                print("ate self")

    def make_snake_longer(self):
        """
        make the snake longer
        """
        i = Turtle()
        i.shape("square")
        i.penup()
        # i.color((rnd.randint(1, 255), rnd.randint(1, 255), rnd.randint(1, 255)))
        i.color("white")
        direction_of_last = self.snake[self.snake_size - 1].heading()
        position_of_last_x = self.snake[self.snake_size - 1].xcor()
        position_of_last_y = self.snake[self.snake_size - 1].ycor()

        if direction_of_last == 0:  # east
            i.setposition(-20 + position_of_last_x, position_of_last_y)
        elif direction_of_last == 90:  # north
            i.setposition(position_of_last_x, -20 + position_of_last_y)
        elif direction_of_last == 180:  # west
            i.setposition(20 + position_of_last_x, position_of_last_y)
        else:  # south
            i.setposition(position_of_last_x, 20 + position_of_last_y)
        i.speed(0)
        self.snake.append(i)
        self.snake_size += 1

    def get_snake_size(self):
        """
        returns length of SNAKE_SIZE
        """
        return len(self.snake)

    def start_snake(self):
        """
        start the beginning of the snake by creating three turtle objects
        """
        move_left = 0
        while self.get_snake_size() < 3:
            self.snake_size += 1
            i = Turtle()
            i.shape("square")
            i.penup()
            # i.color((rnd.randint(1, 255), rnd.randint(1, 255), rnd.randint(1, 255)))
            i.color("white")
            i.setx(-move_left)
            move_left += 20
            i.speed(0)
            self.snake.append(i)

    def move_forward(self, poz):
        """
        replaces the position of snake parts after the head
        """
        self.did_snake_eat_self()
        if self.game_over is False:
            self.start_moving = True
            self.snake[0].forward(20)
            for idx in range(1, self.get_snake_size()):
                temp = self.snake[idx].position()
                self.snake[idx].goto(poz)
                poz = temp

    def move_north(self):
        """
        function moves the snake north by 20 px
        """
        if self.snake[0].heading() != 270:
            prev_position = self.snake[0].position()
            self.snake[0].seth(90)
            self.move_forward(prev_position)

    def move_south(self):
        """
        function moves the snake south by 20 px
        """
        if self.snake[0].heading() != 90:
            prev_position = self.snake[0].position()
            self.snake[0].seth(270)
            self.move_forward(prev_position)

    def move_west(self):
        """
        function moves the snake south by 20 px
        """
        if self.snake[0].heading() != 0:
            prev_position = self.snake[0].position()
            self.snake[0].seth(180)
            self.move_forward(prev_position)

    def move_east(self):
        """
        function moves the snake south by 20 px
        """
        if self.snake[0].heading() != 180:
            prev_position = self.snake[0].position()
            self.snake[0].seth(0)
            self.move_forward(prev_position)

    def keep_moving_forward(self):
        """function is called continuously to keep snake moving
        in the direction it is already facing"""
        direction = self.snake[0].heading()
        if direction == 0:
            self.move_east()
        elif direction == 90:
            self.move_north()
        elif direction == 180:
            self.move_west()
        else:
            self.move_south()
