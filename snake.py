from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
        
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()       # 不要讓windows上面有線條
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)  #let the snake body out of the window
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def move(self):
        # 如何讓snake移動?
        # range的第一個agrument是起始點， 再來是終點， 最後是距離
        # 為了讓後面的snake body重複前一個身體走過的路，後面位置的處理方式是找出上一個位置的(x,y)
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
        
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
            