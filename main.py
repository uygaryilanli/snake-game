from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkSeaGreen")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on_game = True

while is_on_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.add_score()
    
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snakes()
    
    
    for segment in snake.snakes[1:]: #snake.head i atlaması için yazdık
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snakes()


screen.exitonclick()