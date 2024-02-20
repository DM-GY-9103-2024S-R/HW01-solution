def setup():
    size(400, 400)
    colorMode(HSB, 255, 255, 255)

def drawTarget(x, y, r, g, b): 
    noStroke()
    fill(r, g, b)
    ellipse(x, y, 100, 100)

def draw():
    background(255)
    for i in range(0, 10, 1):
        x = 200 + cos(i * 0.15 + frameCount * 0.05) * 150
        y = 200 + sin(i * 0.15 + frameCount * 0.05) * 150
        r = 25 * i
        drawTarget(x, y, r, 255, 255)
