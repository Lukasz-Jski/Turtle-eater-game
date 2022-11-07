from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SLEEP_TIME = 0.35

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("TURTLE EATER")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if SLEEP_TIME != 0.05:
            SLEEP_TIME -= 0.05
            SLEEP_TIME = round(SLEEP_TIME, 2)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()
        SLEEP_TIME = 0.35

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
            SLEEP_TIME = 0.35

screen.exitonclick()
