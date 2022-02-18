from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score=0
        self.highscore=0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.write(f'score :{self.score}' ,align=ALIGNMENT ,font=FONT)

    #def game_over(self):
     #   self.goto(0,0)
      #  self.write('GAME OVER', align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update()




    def increase_score(self):
        self.score+=1

        self.update()
