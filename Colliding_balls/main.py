import tkinter as tk
from math import *
from random import *
from ball import *


def timer_cycle():
    global window, balls_array
    for ball in balls_array:
        ball.move()

        for wall in [(0, None), (900, None), (None, 0), (None, 600)]:
            if ball.collide_with_wall(wall):
                ball.bounce_off_wall(wall)

        for ball2 in balls_array:
            if ball2 != ball:
                if ball.collide_with_ball(ball2):
                    ball.bounce_off_ball(ball2)


    window.after(100, timer_cycle)
    return


window = tk.Tk()
window.geometry("900x600")
canv = tk.Canvas(window, width=900, height=600)
canv.pack()

# рисуем шары.

n_balls = 5
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'brown', 'pink']
balls_array = []

for i in range(n_balls):
    balls_array.append(Ball(canv,
                            randint(50, 850),
                            randint(50, 550),
                            randint(15, 50),
                            randint(1, 10),
                            randint(1, 10),
                            choice(colors)))


window.after(100, timer_cycle)
window.mainloop()

#if __name__ == '__main__':
#    start_game()