import math


class Ball:

    def __init__(self, canv, x, y, radius, dx, dy, color):
        self.canv = canv
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.color = color
        self.object = canv.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)
        return

    def move(self):
        self.canv.move(self.object, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        return

    def collide_with_wall(self, wall):
        if wall[1] is None and abs(self.x - wall[0]) <= self.radius:
            return True

        if wall[0] is None and abs(self.y - wall[1]) <= self.radius:
            return True

        return False

    def bounce_off_wall(self, wall):
        if wall[1] is None:
            self.dx *= -1
        else:
            self.dy *= -1
        return

    def collide_with_ball(self, other_ball):
        if math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2) <= (self.radius + other_ball.radius):
            return True
        return False

    def bounce_off_ball(self, other_ball):
        fi = math.atan((self.y - other_ball.y)/(self.x - other_ball.x))
        v1 = math.sqrt(self.dx**2 + self.dy**2)
        v2 = math.sqrt(other_ball.dx**2 + other_ball.dy**2)
        
        dx1_star = self.dx * math.sin(fi)-self.dy * math.cos(fi)
        dy1_star = self.dx * math.cos(fi)-self.dy * math.sin(fi)
        dx2_star = other_ball.dx * math.sin(fi)-other_ball.dy2 * math.cos(fi)
        dy2_star = other_ball.dx * math.cos(fi) - other_ball.dy * math.sin(fi)
        return
    

