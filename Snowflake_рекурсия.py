import turtle


def move_turtle(cmd):
    if cmd == 'F':
        turtle.forward(a)
    elif cmd == 'L':
        turtle.left(60)
    else:
        turtle.right(120)
    return


def kokh_star(moves_in, n):
    if n == 0:
        return moves_in
    else:
        moves_out = []
        for move in moves_in:
            if move == 'F':
                moves_out.extend(kokh_star(('F', 'L', 'F', 'R', 'F', 'L', 'F'), n - 1))
            else:

                moves_out.append(move)
    return moves_out


# начальные значения

n = 2
a = int(500 / (3 ** n))

turtle.Screen().setup(1000, 800, 0, 0)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# Launch turtle
for move in kokh_star(('F', 'R', 'F', 'R', 'F'), n):
    move_turtle(move)

turtle.Screen().exitonclick()
