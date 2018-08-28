GRAVITY = PVector(0, 0.5)
HEIGHT = 360
WIDTH = 640

class Player:
    
    def __init__(self, startX = 100, startY = 100, cLen = 50, cWid = 50):
        self.cLen = cLen
        self.cWid = cWid
        self.location = PVector(startX, startY, 100)
        self.velocity, self.movement = PVector(0, 0), [0, 0]
        self.walkSpeed = 4
        self.jumpSpeed = 13
        self.ground = HEIGHT - 5
        self.ceiling = 0
    
    def updatePosition(self):
        
        if self.location.y + self.cLen // 2 <= self.ground:
            self.velocity.y += GRAVITY.y
        
        if not ((self.location.y + self.velocity.y) + self.cLen // 2 <= self.ground):
            self.velocity.y = 0
            self.location.y = self.ground - self.cLen // 2
        if not self.location.y - self.cLen // 2 + self.velocity.y >= self.ceiling:
            self.velocity.y = 0
            self.location.y = self.ceiling + self.cLen // 2
            
        if self.location.y + self.cLen // 2 < self.ground and self.movement[1] < 0:
            self.velocity.y -= self.movement[1]
            
        if self.location.y + self.cLen // 2 == self.ground and self.movement[1] > 0:
            self.velocity.y = -self.jumpSpeed
        
        self.velocity.x = self.walkSpeed * self.movement[0]
        
        self.location.add(self.velocity)
        
        if (self.location.x + self.cWid // 2 >= width):
            self.location.x = width - self.cWid // 2
        if (self.location.x - self.cWid // 2 <= 0):
            self.location.x = self.cWid // 2
    
    def updatePositionMovement(self, direction, isPressed):
        if isPressed:
            if direction == "up":
                self.movement[1] = 1
            elif direction == "down":
                self.movement[1] -= 1
            elif direction == "left":
                self.movement[0] = -1
            elif direction == "right":
                self.movement[0] = 1
        
        else:
            if direction == "up":
                self.movement[1] = 0
            elif direction == "down":
                self.movement[1] = 0
            elif direction == "left" and self.movement[0] != 1:
                self.movement[0] = 0
            elif direction == "right" and self.movement[0] != -1:
                self.movement[0] = 0
        
    def drawPlayer(self):
        stroke(255)
        strokeWeight(1)
        fill(0, 0, 255)
        rectMode(CENTER)
        rect(self.location.x, self.location.y, self.cLen, self.cWid)
        
    def findBoundY(self, platform, findCeiling):
        hitbox = platform.getRect()
        if (self.cWid // 2 + self.location.x >= hitbox[0] and
            self.location.x - self.cWid // 2 <= hitbox[0] + hitbox[2]):
            if self.location.y + self.cLen // 2 <= hitbox[1] and findCeiling:
                self.ground = hitbox[1]
                
            if self.location.y - self.cLen // 2 >= hitbox[1] + hitbox[3] and not findCeiling:
                self.ceiling = hitbox[1] + hitbox[3]
                
        
class Platform:
    def __init__(self, x, y, pWid, pLen, name):
        self.x = x
        self.y = y
        self.pWid = pWid
        self.pLen = pLen
        self.name = name
    
    def __str__(self):
        return self.name
    
    def drawPlatform(self):
        stroke(255)
        strokeWeight(1)
        fill(0)
        rectMode(CORNER)
        rect(self.x, self.y, self.pWid, self.pLen)
    
    def getRect(self):
        return [self.x, self.y, self.pWid, self.pLen]



player = Player(startX = 10, startY = 10)


ground = Platform(0, HEIGHT - 1, WIDTH, 1, "Ground")
platform1 = Platform(100, HEIGHT * 0.75, 100, 7, "Platform 1")
platform2 = Platform(300, HEIGHT * 0.5, 100, 7, "Platform 2")
platform3 = Platform(425, HEIGHT * 0.5 + 20, 10, HEIGHT * 0.5 - 25, "Platform 3")
ceiling = Platform(0, -1, WIDTH, 1, "Ceiling")

platformList = [ground, platform1, platform2, platform3, ceiling]

def setup():
    size(640, 360)
    

def draw():
    global platformList
    background(0)
    
    textSize(16)
    fill(255, 255, 255)
    text("Priority: " + ' '.join([str(platform) for platform in platformList]), 10, 30)
    
    
    player.drawPlayer()
    
    for p in range(1, len(platformList) + 1):
        platformList[p - 1].drawPlatform()
        player.findBoundY(platformList[p - 1], True)
        player.findBoundY(platformList[-p], False)
    player.updatePosition()

def keyPressed():
    
    if keyCode == UP or key == 'w':
        player.updatePositionMovement("up", True)
    if keyCode == DOWN or key == 's':
        player.updatePositionMovement("down", True)
    if keyCode == LEFT or key == 'a':
        player.updatePositionMovement("left", True)
    if keyCode == RIGHT or key == 'd':
        player.updatePositionMovement("right", True)
        
def keyReleased():
    if keyCode == UP or key == 'w':
        player.updatePositionMovement("up", False)
    if keyCode == DOWN or key == 's':
        player.updatePositionMovement("down", False)
    if keyCode == LEFT or key == 'a':
        player.updatePositionMovement("left", False)
    if keyCode == RIGHT or key == 'd':
        player.updatePositionMovement("right", False)
