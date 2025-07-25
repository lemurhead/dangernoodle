from tkinter import *
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
score = 0
score_text = canvas.create_text(50, 20, text="Score: 0", font=('Helvetica', 14), fill='blue')
#defines the balls behavior
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        #ball starting positon
        self.canvas.move(self.id,245,100)
        #sets randomized horizontal speed
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        #sets vertical speed
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #sets for ending game if true
        self.hit_bottom = False
    #ensures overlap of horizontal and vertical parts of the paddle and ball if either returns false then no collison
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                #adds paddle horizontal momentum onto ball
                self.x += self.paddle.x
                return True
        return False
    #Adds score and rules for the the ball to follow on canvas
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        #sets self.hit_bottom tto true if the ball hits the bottom thereby ending the game
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        #adds score if paddle hits ball
        if self.hit_paddle(pos) == True:
            self.y = -3
            global score
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
#creating paddle and adding key controls along with speed of paddle
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        #sets arrow keys to control the movement
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    #gives coordinates and checks if paddle is touching wall and stops it
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    #sets the amount that key moves with turn left or turn right
    def turn_left(self, evt):
        self.x = -4
    def turn_right(self, evt):
        self.x = 4
                
#adding objects
paddle = Paddle(canvas, 'red')
ball = Ball(canvas, paddle, 'green')

#defining game over screen
def show_game_over():
    canvas.create_text(250, 200, text="GAME OVER", font=('Helvetica', 30), fill='red')
    tk.update()
#starting game loop and stops and adds game over if the ball hits the bottom
def game_loop():
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
        #update every 10 miliseconds
        tk.after(10, game_loop)
    else:
        canvas.create_text(250, 200, text="GAME OVER", font=('Helvetica', 30), fill='red')

game_loop()
tk.mainloop()
