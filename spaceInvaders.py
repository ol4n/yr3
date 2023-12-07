
# Name: Olan Kelleher
# spaceship image: <a href="https://www.flaticon.com/free-icons/space-invaders" title="space invaders icons">Space invaders icons created by Smashicons - Flaticon</a>
# enemy image: https://www.pngegg.com/en/png-ffmzl/download?width=80
# missile image: https://www.pngegg.com/en/png-dkpis/download?width=40
import sys, pygame, math

class MyGame(object):

    def __init__(self):
        
        pygame.init()
        
        self._size = self._width, self._height = 560, 480
        self._black = 0, 0, 0
        
        self._screen = pygame.display.set_mode(self._size)

        self._shipview = pygame.image.load("ca2/space_ship.png")
        self._shipmodel = ShipState(210, 350, self._width, 3)

        self._enemyview1 = pygame.image.load("ca2/enemy.png")
        self._enemymodel1 = Enemy(self._width-80, 0, 0.1)

        self._enemyview2 = pygame.image.load("ca2/enemy.png")
        self._enemymodel2 = Enemy(800, 0, 0.1)

        self._enemyview3 = pygame.image.load("ca2/enemy.png")
        self._enemymodel3 = Enemy(1320, 0, 0.1)

        self._missileList = []

    def rungame(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            self._shipmodel.handleMoveLeft()

                    if event.key == pygame.K_RIGHT:
                        self._shipmodel.handleMoveRight()

                    if event.key == pygame.K_SPACE:
                        missile = Missile(self._shipmodel.getXPos())
                        self._missileList.append(missile)

                if event.type == pygame.KEYUP:
                    self._shipmodel.handleStopMove()

            if youreHit(self._shipmodel.getXPos(), self._shipmodel.getYPos(), self._enemymodel1.getXPos(), self._enemymodel1.getYPos()):
                sys.exit()
            if youreHit(self._shipmodel.getXPos(), self._shipmodel.getYPos(), self._enemymodel2.getXPos(), self._enemymodel2.getYPos()):
                sys.exit()
            if youreHit(self._shipmodel.getXPos(), self._shipmodel.getYPos(), self._enemymodel3.getXPos(), self._enemymodel3.getYPos()):
                sys.exit()
            
            self._screen.fill(self._black)
            self._screen.blit(self._shipview, (self._shipmodel.getXPos(), self._shipmodel.getYPos()))
            i = 0
            while i < len(self._missileList):
                self._missileList[i].moveMissile()
                self._screen.blit(self._missileList[i].getIcon(), (self._missileList[i].getXPos(), self._missileList[i].getYPos()))
                if enemyHit(self._missileList[i].getXPos(), self._missileList[i].getYPos(), self._enemymodel1.getXPos(), self._enemymodel1.getYPos()):
                    self._enemymodel1.setXPos(1600)
                if enemyHit(self._missileList[i].getXPos(), self._missileList[i].getYPos(), self._enemymodel2.getXPos(), self._enemymodel2.getYPos()):
                    self._enemymodel2.setXPos(1200)
                if enemyHit(self._missileList[i].getXPos(), self._missileList[i].getYPos(), self._enemymodel3.getXPos(), self._enemymodel3.getYPos()):
                    self._enemymodel3.setXPos(2000)
                i += 1

            self._screen.blit(self._enemyview1, (self._enemymodel1.getXPos(), self._enemymodel1.getYPos()))
            self._enemymodel1.enemyMovement()

            self._screen.blit(self._enemyview2, (self._enemymodel2.getXPos(), self._enemymodel2.getYPos()))
            self._enemymodel2.enemyMovement()

            self._screen.blit(self._enemyview3, (self._enemymodel3.getXPos(), self._enemymodel3.getYPos()))
            self._enemymodel3.enemyMovement()
            
            
            pygame.display.flip()

class Missile(object):
    def __init__(self, xpos):
        self._xPos = xpos + 45 
        self._yPos = 350
        self._icon = pygame.image.load("ca2/missile.png")
        self._shipchange = 1

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def moveMissile(self):
            self._yPos -= self._shipchange

    def getIcon(self):
        return self._icon

class ShipState(object):
    def __init__(self, xpos, ypos, maxxpos, change):
        self._xPos = xpos
        self._yPos = ypos
        self._maxXPos = maxxpos
        self._shipchange = change

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def handleMoveRight(self):
        
        if self._xPos + self._shipchange < self._maxXPos-120:
            self._xPos += self._shipchange

    def handleMoveLeft(self):

        if self._xPos - self._shipchange > 0:
            self._xPos -= self._shipchange

    def handleStopMove(self):
        
        self._xPos = self._xPos

class Enemy(object):
    def __init__(self, xpos, ypos, change):
        self._xPos = xpos
        self._yPos = ypos
        self._enemychange = change

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def setXPos(self, xpos):
        self._xPos = xpos

    def enemyMovement(self):
        self._xPos -= self._enemychange
        if self._xPos + 80 < 0:
            self._xPos = 560
            self._yPos += 80

def youreHit(ship_x, ship_y, enemy_x, enemy_y):
    distance = math.sqrt((math.pow(ship_x - enemy_x,2)) +
                         (math.pow( ship_y - enemy_y,2)))
    if distance < 80:
        return True
    else:
        return False 

def enemyHit(missile_x, missile_y, enemy_x, enemy_y):
    distance = math.sqrt((math.pow(missile_x - enemy_x,2)) +
                         (math.pow( missile_y - enemy_y,2)))
    if distance < 50:
        return True
    else:
        return False 

if __name__ == "__main__":
    mygame = MyGame()
    mygame.rungame()