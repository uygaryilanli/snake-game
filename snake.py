from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    
    def __init__(self) -> None:
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)
    
    
    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("black")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)
    
    
    def reset_snakes(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
    
    
    def extend(self):
        #add a new snake
        self.add_snake(self.snakes[-1].position())
    
    
    def move(self):
        for num_snakes in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[num_snakes - 1].xcor()
            new_y = self.snakes[num_snakes - 1].ycor()
            self.snakes[num_snakes].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)