import random
from tkinter import *

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colours = ['red', 'green', 'blue', 'yellow', 'black', 'violet', 'brown', 'orange']


def draw_circle():
    x = random.randint(1, 800)
    y = random.randint(1, 600)
    r = random.randint(1, 100)
    c = random.randint(0, len(colours) - 1)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=colours[c])
    root.after(100, draw_circle)


draw_circle()

root.mainloop()
