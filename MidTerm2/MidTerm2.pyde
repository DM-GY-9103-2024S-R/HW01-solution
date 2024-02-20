NUM_PETALS = 10
NUM_STEMS = 16
SUN_X = 56

obj_flowerpetal = []
obj_flowerstem = []

class flowerstem:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy
        self.y0 = yy
        self.y1 = self.y0 - height * random(0.25, 0.75)
        self.density = int(random(2, 16))
        self.col = random(180, 360)

    def display(self):
        stroke("#8dd043")
        fill("#5f7546")
        ellipse(self.x, self.y, 30, 30)
        line(self.x, self.y0, self.x, self.y)

        petal_angle = 0
        for i in range(0, self.density):
            xflowerpetal = self.x + sin(petal_angle) * 30
            yflowerpetal = self.y + cos(petal_angle) * 30
            pushMatrix()
            translate(xflowerpetal, yflowerpetal)
            rotate((PI/2) - petal_angle)
            stroke(self.col, 100, 100)
            fill(self.col, 70, 50)
            ellipse(0, 0, 20, 10)
            line(-15, 0, 0, 0)
            popMatrix()
            petal_angle += TWO_PI/self.density

    def move(self):
        self.y += (self.y1 - self.y) / 5

class flowerpetal:
    def __init__(self, xx, yy, cc):
        self.x = xx
        self.y = yy
        self.hsp = random(-10, 10)
        self.vsp = random(-10, 10)
        self.gravity = 0.2
        self.speed = random(0.05, 0.2)
        self.max = random(4, 5)
        self.dead = 0
        self.col = cc

    def display(self):
        stroke(self.col, 100, 100)
        fill(self.col, 70, 50)
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.x / 50)
        ellipse(0, 0, 20, 10)
        line(-15, 0, 0, 0)
        popMatrix()

    def move(self):
        self.vsp += self.gravity
        self.vsp = constrain(self.vsp, -self.max, self.max)

        self.x += self.hsp
        self.y += self.vsp

        if self.y > height:
            self.dead = 1

def setup():
    size(1000, 700)
    colorMode(HSB, 360, 100, 100)

    for _ in range(0, NUM_PETALS):
        obj_flowerpetal.append(flowerpetal(width/2, width/4, 0))

    for _ in range(0, NUM_STEMS):
        obj_flowerstem.append(flowerstem(width * random(0.05, 0.95), height))


def draw():
    background(200, 95, 80)

    #create sun
    fill("#FFFF00")
    noStroke()
    circle(SUN_X, height / 6, 100)

    # create green grass
    fill("#486F38")
    rect(0, 0.7 * height, width, 0.3 * height)

    for fp in obj_flowerpetal:
        if fp.dead != 1:
            fp.move()
            fp.display()

    for fs in obj_flowerstem:
        fs.move()
        fs.display()


def mousePressed():
    del obj_flowerpetal[:]
    del obj_flowerstem[:]

    for _ in range(0, NUM_PETALS):
        obj_flowerpetal.append(flowerpetal(mouseX, mouseY, 0))
 
    for _ in range(0, NUM_STEMS):
        obj_flowerstem.append(flowerstem(width * random(0.05, 0.95), height))
