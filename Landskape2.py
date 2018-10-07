import graphics as gr

window = gr.GraphWin("Russian game", 1000, 500)

# Рисуем небо
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 250))
sky.setFill('blue')
sky.draw(window)

# Рисуем солнце
sun = gr.Circle(gr.Point(750, 100), 50)
sun.setFill('yellow')
sun.draw(window)

# Рисуем облака
# 5 облаков

clouds = [gr.Circle(gr.Point(90, 75), 25), gr.Circle(gr.Point(120, 75), 25), gr.Circle(gr.Point(75, 100), 25),
          gr.Circle(gr.Point(105, 100), 25), gr.Circle(gr.Point(135, 100), 25), gr.Circle(gr.Point(590, 95), 25),
          gr.Circle(gr.Point(620, 95), 25), gr.Circle(gr.Point(575, 120), 25), gr.Circle(gr.Point(605, 120), 25),
          gr.Circle(gr.Point(635, 120), 25), gr.Circle(gr.Point(790, 105), 25), gr.Circle(gr.Point(820, 105), 25),
          gr.Circle(gr.Point(775, 130), 25), gr.Circle(gr.Point(805, 130), 25), gr.Circle(gr.Point(735, 130), 25)]

for cloud in clouds:
    cloud.setFill('white')
    cloud.draw(window)

# Рисуем землю
ground = gr.Rectangle(gr.Point(0, 250), gr.Point(1000, 500))
ground.draw(window)
ground.setFill('dark grey')

# Рисуем дом
# Стены, окна, крыши
house = gr.Rectangle(gr.Point(250, 150), gr.Point(450, 350))
house.draw(window)
house.setWidth(5)
house.setFill('grey')

glasses = [gr.Rectangle(gr.Point(300, 190), gr.Point(350, 240)), gr.Rectangle(gr.Point(350, 190), gr.Point(400, 240)),
           gr.Rectangle(gr.Point(300, 240), gr.Point(350, 290)), gr.Rectangle(gr.Point(350, 240), gr.Point(400, 290))]

for glass in glasses:
    glass.setFill('yellow')
    glass.setWidth(5)
    glass.draw(window)

roof = gr.Polygon(gr.Point(250, 150), gr.Point(450, 150), gr.Point(350, 80))
roof.setFill('brown')
roof.setWidth(5)
roof.draw(window)

# Рисуем дерево
# Ствол, хвоя (3 уровня)

trunk = gr.Rectangle(gr.Point(790, 380), gr.Point(800, 430))
trunk.setWidth(5)
trunk.setFill('brown')
trunk.draw(window)

needles = [gr.Polygon(gr.Point(710, 380), gr.Point(795, 300), gr.Point(880, 380)),
           gr.Polygon(gr.Point(710, 330), gr.Point(795, 250), gr.Point(880, 330)),
           gr.Polygon(gr.Point(710, 280), gr.Point(795, 200), gr.Point(880, 280))]

for needle in needles:
    needle.setFill('green')
    needle.setWidth(5)
    needle.draw(window)

window.getMouse()
window.close()
