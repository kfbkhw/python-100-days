from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Imported Classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Maneuver
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Game Setting
game_on = True
while game_on:
    screen.update()
    snake.move()
    time.sleep(0.2)

# Detects Collision w/ Food
    if snake.head.distance(food) < 15:
        scoreboard.new_score()
        snake.extend()
        food.refresh()

# Detects Collision w/ Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

# Detects Collision w/ Wall
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

# Game Exit
screen.exitonclick()
