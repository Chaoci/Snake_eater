from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreborad
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() # 蛇蛇動畫 詳見 snake.py
food = Food()  # 食物點點 詳見 food.py
scoreboard = Scoreborad() #記分板面 詳見scoreboard.py

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    # 為了讓蛇頭碰到食物時能夠判斷吃到食物 使用 Turtle.distance
    # let the snake can judge whether eat the food or not
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.extend()
    # 讓蛇蛇撞到牆壁會掛掉
    # game over as the snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # 蛇蛇撞到自己身體也會掛掉
    # if snake hit itself would be game over as well
    for segment in snake.segments[1:]:
        # if segment == snake.head: # 因為每個segnent實際上都小於10的距離而且後一個會走到前一個的位置，因次直接pass
        #     pass
        if snake.head and snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


    snake.move()
screen.exitonclick()