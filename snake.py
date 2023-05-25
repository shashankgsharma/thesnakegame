import turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.D = 0
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(3):
            start_x = 0
            start_y = 0
            self.add_segment((start_x, start_y))
            start_x -= MOVE_DISTANCE

    def add_segment(self, position):
        snake = turtle.Turtle(shape="square")
        snake.color("black")
        snake.speed("slowest")
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            next_pos = self.snake_segments[seg_num - 1].pos()
            self.snake_segments[seg_num].goto(next_pos)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

