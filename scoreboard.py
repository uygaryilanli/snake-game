from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Score(Turtle):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("!!!BULUNDUĞUNUZ DOSYA KONUMUNU GİRİN!!!/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    
    
    def update_score(self):
        self.clear()
        self.write(f"Score Table: {self.score} | High Score: {self.high_score}", align=ALIGNMENT , font=FONT)
    
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("!!!BULUNDUĞUNUZ DOSYA KONUMUNU GİRİN!!!/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
                data.close()
        self.score = 0
        self.update_score()
    
    
    def add_score(self):
        self.score += 1
        self.update_score()