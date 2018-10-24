import turtle
import graphics as gr


def move_turtle(cmd):
    if cmd == 'F':
        turtle.forward(a)
    elif cmd == 'L':
        turtle.left(60)
    else:
        turtle.right(120)
    return


window = gr.GraphWin("Russian game", 1000, 500)

# начальные значения
n = 5
a = int(500 / (3 ** n))

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# программа правильного треугольника
moves = ['F', 'R', 'F', 'R', 'F']

# цикл из n проходов
for i in range(n):
    # замена всех F на комбинацию 'FLFRFLF'
    moves2 = []
    for move in moves:
        if move == 'F':
            moves2.extend(('F', 'L', 'F', 'R', 'F', 'L', 'F'))
        else:
            moves2.append(move)
    moves = moves2

# Launch turtle
for move in moves:
    move_turtle(move)

window.getMouse()
window.close()
