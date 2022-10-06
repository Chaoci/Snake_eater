from turtle import Turtle
AlIGNMENT ="center"
FONT = ("Courier", 20, "normal")
class Scoreborad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day20-Snake_Game/data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write( f"Score: {self.score}, Hight Score: {self.high_score}",
            align='center', 
            font=('Arial', 24, 'normal'))
        
        
    def update_score(self):
        self.clear()
        self.write( f"Score: {self.score}, Hight Score: {self.high_score}",
            align='center', 
            font=('Arial', 24, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day20-Snake_Game/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0   # reset the points
        self.update_score()