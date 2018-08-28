GRAVITY = PVector(0, 0.5)

class Player:
    
    def __init__(self, cLen = 50, cWid = 50):
        self.cLen = cLen
        self.cWid = cWid
        self.location = PVector(100, 100)
        self.velocity, self.movement = PVector(0, 0), [0, 0]
        self.walkSpeed = 4
        self.jumpSpeed = 12

    def updatePlayer(self):
        
        if self.location.y + self.cLen // 2 <= height:
            self.velocity.add(GRAVITY)
            if self.movement[1] < 0:
                self.velocity.y -= self.movement[1]
            
        else:
            self.velocity.y = 0
            self.location.y = height - self.cLen // 2
            
        if self.location.y + self.cLen // 2 == height and self.movement[1] > 0:
            self.velocity.y = -self.jumpSpeed
        
        self.velocity.x = self.walkSpeed * self.movement[0]
        
        self.location.add(self.velocity)
        
        if (self.location.x + self.cWid // 2 >= width):
            self.location.x = width - self.cWid // 2
        if (self.location.x - self.cWid // 2 <= 0):
            self.location.x = self.cWid // 2
        
        
    
    def updatePlayerMovement(self, direction, isPressed):
        if isPressed:
            if direction == "up":
                self.movement[1] += 1
            elif direction == "down":
                self.movement[1] -= 1
            elif direction == "left" and self.movement[0] > -2:
                self.movement[0] -= 1
            elif direction == "right" and self.movement[0] < 2:
                self.movement[0] += 1
        
        else:
            if direction == "up":
                self.movement[1] = 0
            elif direction == "down":
                self.movement[1] = 0
            elif direction == "left":
                self.movement[0] = 0
            elif direction == "right":
                self.movement[0] = 0
        print(self.movement)
    def drawPlayer(self):
        stroke(255)
        strokeWeight(2)
        fill(127)
        rectMode(CENTER)
        rect(self.location.x, self.location.y, self.cLen, self.cWid)

player = Player()        
        
def setup():
    size(640, 360)

def draw():
    background(0)
    
    # Character defining
    '''
    '''
    player.drawPlayer()
    player.updatePlayer()
    
def keyPressed():
    
    if keyCode == UP or key == 'w':
        print("Up")
        player.updatePlayerMovement("up", True)
    if keyCode == DOWN or key == 's':
        print("Down")
        player.updatePlayerMovement("down", True)
    if keyCode == LEFT or key == 'a':
        print("Left")
        player.updatePlayerMovement("left", True)
    if keyCode == RIGHT or key == 'd':
        print("Right")
        player.updatePlayerMovement("right", True)
        
def keyReleased():
    if keyCode == UP or key == 'w':
        player.updatePlayerMovement("up", False)
    if keyCode == DOWN or key == 's':
        player.updatePlayerMovement("down", False)
    if keyCode == LEFT or key == 'a':
        player.updatePlayerMovement("left", False)
    if keyCode == RIGHT or key == 'd':
        player.updatePlayerMovement("right", False)
