x = 240
y = 10
speed = 0
gravity = 0.4
    
def setup():
    
    size(480, 270)

def draw():
    global y, speed
    background(0)
    
    fill(175)
    stroke(0)
    rectMode(CENTER)
    rect(x, y, 30, 30)
    
    y = y + speed
    
    speed = speed + gravity

    if y + 15 >= height:
         y = height - 15
