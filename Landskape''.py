import graphics as gr


def draw_tree():
    # Ствол, хвоя (3 уровня)
    draw_trunk(790, 380)

    for n in range(3):
        draw_needles(710, 300 - n * 50)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1000, 250))
    sky.setFill('blue')
    sky.draw(window)


def draw_sun(x, y):
    o_sun = gr.Circle(gr.Point(x, y), 50)
    o_sun.setFill('yellow')
    o_sun.setOutline('yellow')
    o_sun.draw(window)
    return o_sun


def draw_ground():
    o_ground = gr.Rectangle(gr.Point(0, 250), gr.Point(1000, 500))
    o_ground.draw(window)
    o_ground.setFill('dark grey')


def draw_cloud(x, y):
    o_cloud = gr.Circle(gr.Point(x, y), 25)
    o_cloud.setFill('white')
    o_cloud.draw(window)
    return o_cloud


def draw_house():
    o_house = gr.Rectangle(gr.Point(250, 150), gr.Point(450, 350))
    o_house.draw(window)
    o_house.setWidth(5)
    o_house.setFill('grey')

    o_glasses = [gr.Rectangle(gr.Point(300, 190), gr.Point(350, 240)),
                 gr.Rectangle(gr.Point(350, 190), gr.Point(400, 240)),
                 gr.Rectangle(gr.Point(300, 240), gr.Point(350, 290)),
                 gr.Rectangle(gr.Point(350, 240), gr.Point(400, 290))]

    for glass in o_glasses:
        glass.setFill('yellow')
        glass.setWidth(5)
        glass.draw(window)

    o_roof = gr.Polygon(gr.Point(250, 150), gr.Point(450, 150), gr.Point(350, 80))
    o_roof.setFill('brown')
    o_roof.setWidth(5)
    o_roof.draw(window)


def draw_trunk(x, y):
    o_trunk = gr.Rectangle(gr.Point(x, y), gr.Point(x + 10, y + 100))
    o_trunk.setWidth(5)
    o_trunk.setFill('brown')
    o_trunk.draw(window)


def draw_needles(x, y):
    o_needles = gr.Polygon(gr.Point(x,       y + 80),
                           gr.Point(x + 85,  y),
                           gr.Point(x + 170, y + 80))
    o_needles.setFill('green')
    o_needles.setWidth(5)
    o_needles.draw(window)


window = gr.GraphWin("Landscape", 1000, 500)

# Рисуем небо
draw_sky()

# Рисуем землю
draw_ground()

# Рисуем солнце
sun = draw_sun(750, 100)

# Рисуем облака
clouds = list()

clouds.append(draw_cloud(90, 75))
clouds.append(draw_cloud(120, 75))

for i in range(3):
    clouds.append(draw_cloud(75 + i * 30, 100))

clouds.append(draw_cloud(590, 95))
clouds.append(draw_cloud(620, 95))

for i in range(3):
    clouds.append(draw_cloud(575 + i * 30, 120))

for i in range(2):
    clouds.append(draw_cloud(790 + i * 30, 105))

for i in range(3):
    clouds.append(draw_cloud(745 + i * 30, 130))

# Рисуем дом
# Стены, окна, крыши
draw_house()

# Рисуем дерево
draw_tree()

##############################################

while True:
    gr.time.sleep(0.05)
    sun.move(-5, 0)

    sun_center = sun.getCenter()
    if sun_center.getX() < 0:
        sun.move(1000, 0)

    for cloud in clouds:
        cloud.move(20, 0)
        if cloud.getCenter().getX() > 1000:
            cloud.move(-1000, 0)
