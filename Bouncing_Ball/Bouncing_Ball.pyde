

location, velocity, gravity = None, None, None

def setup():
    global location, velocity, gravity
    size(640, 360)
    location = PVector(100, 100)
    velocity = PVector(1.5, 2.1)
    gravity = PVector(0, 0.2)

def draw():
    global location, velocity, gravity
    background(0)
    
    location.add(velocity)
    
    velocity.add(gravity)
    
    if (location.x > width) or (location.x < 0):
        velocity.x = velocity.x * -1
        
    if location.y > height:
        velocity.y = velocity.y * -0.95
        location.y = height
        
    stroke(255)
    strokeWeight(2)
    fill(127)
    ellipse(location.x, location.y, 48, 48)
