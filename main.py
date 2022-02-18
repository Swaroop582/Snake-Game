from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food =Food()
scoreboad=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision of food and snake

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboad.increase_score()

    # detect collision with wall

    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        scoreboad.game_over()

    # detect collision with tail
    # if head collides with any other segment then end game

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False













screen.exitonclick()













