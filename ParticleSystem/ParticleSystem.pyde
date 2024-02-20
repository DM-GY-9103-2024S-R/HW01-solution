NUM_PARTICLES = 100
mPs = []

class Particle:
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(random(-3, 3), random(-3, 3))
        self.size = map(abs(self.vel.x), 0, 2, 2, 10)
        self.color = color(random(255), random(255), random(255))

    def update(self):
        self.pos.add(self.vel)
        if self.pos.x < 0 or self.pos.x > width:
            self.vel.x *= -1
        if self.pos.y < 0 or self.pos.y > height:
            self.vel.y *= -1

    def show(self):
        fill(self.color)
        ellipse(self.pos.x, self.pos.y, self.size, self.size)

def setup():
    size(600, 600)
    noStroke()
    for i in range(0, NUM_PARTICLES):
        mPs.append(Particle())

def draw():
    background(0, 10)
    for p in mPs:
        p.update()
        p.show()
