from tkinter import *
from random import  randint


class Ball:
    def __init__(self, x, y, dx, dy):
        self.oval = canvas.create_oval(x, y, x+40, y+40)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        if self.x < 0:
            self.dx = -self.dx
            self.x = 0
        elif self.x > 1000-40:
            self.dx = -self.dx
            self.x = 1000-40
        if self.y < 0:
            self.dy = -self.dy
            self.y = 0
        elif self.y > 600-40:
            self.dy = -self.dy
            self.y = 600-40
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        canvas.move(self.oval, self.dx, self.dy)


def tick_handler2():
    # Отражение от края холста
    for ball in balls_array:
        ball.move()


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler2()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)

########################################################################################

root = Tk()
root.geometry("600x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1)
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

balls_array = []

for i in range(15):
    balls_array.append(
        Ball(randint(0, 100),
             randint(0, 100),
             randint(0, 10),
             randint(0, 10)))

root.mainloop()