from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()

score = 0

screen.update()

screen.listen()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)

time.sleep(1)
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()
        snake.add_to_tail()
        scoreboard.refresh()

    # Detect collision with food
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()
        time.sleep(1)

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            time.sleep(1)
