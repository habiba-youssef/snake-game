from turtle import Turtle

START_SNAKE = ["square1", "square2", "square3"]
MOVE_DISTANCE = 20
COLOUR = "green"
SHAPE = "square"

class Snake:
    def __init__(self):
        self.x = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for square in START_SNAKE:
            square = Turtle(SHAPE)
            square.penup()
            square.color(COLOUR)
            square.setx(self.x)
            self.x -= 20
            self.snake.append(square)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.head.fd(MOVE_DISTANCE)

    def add_to_tail(self):
        new_seg = Turtle(SHAPE)
        new_seg.penup()
        new_seg.color(COLOUR)
        new_seg.goto(self.snake[-1].position())
        self.snake.append(new_seg)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.x = 0
        self.create_snake()
        self.head = self.snake[0]