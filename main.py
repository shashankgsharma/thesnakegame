import turtle
import time
import snake
import food
import random
import scorecard

user_score = 0

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("The Snake Game")
screen.tracer(0)

new_snake = snake.Snake()
turtle.listen()
turtle.onkeypress(new_snake.move_up, key="Up")
turtle.onkeypress(new_snake.move_down, key="Down")
turtle.onkeypress(new_snake.move_left, key="Left")
turtle.onkeypress(new_snake.move_right, key="Right")

snake_food = food.Food()
score_card = scorecard.ScoreCard()

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    score_card.undo()
    score_card.display()
# Detect collision with food
    if new_snake.head.distance(snake_food) < 15:
        score_card.user_score += 1
        new_snake.extend()
        snake_food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Detect collision with wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        is_game_over = True
        score_card.game_over()

# Detect collision with tail
    # If head collides with any segment, then game_over is true
    for segment in new_snake.snake_segments[1:]:
        if new_snake.head.distance(segment) < 10:
            is_game_over = True
            score_card.game_over()

print(f"Thanks, you scored: {score_card.user_score} points.")

screen.exitonclick()
