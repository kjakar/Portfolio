__author__ = 'Alex Jones'

import math
import pygame
import random
import asteroid

blast = pygame.image.load("images//thruster_gradient.png")
boom = pygame.image.load("images//explosion_gradient.png")
ship = pygame.image.load("images//spaceshipM.png")

def dis(x1, y1, x2, y2):
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis

class emmiter(object):
    def __init__(self, x, y, angle):
        self.mAngle = angle # in degrees
        self.mX = x
        self.mY = y
        self.mParticleList = []
        self.mExplosionsList = []

    def updateAngle(self, newAngle):
        self.mAngle = newAngle

    def createExplosion(self, x, y):
        for i in range(200):
            X = x
            Y = y
            number = random.randint(-180,180)
            angle = math.radians(self.mAngle + number)
            size = random.randint(3,11)

            boom = [X,Y,angle,255,size]
            self.mExplosionsList.append(boom)

    def renderExplosion(self, dt, surface):
        for p in self.mExplosionsList:
            # adjust color
            color = boom.get_at((int(p[3]), 0))
            p[3] -= 300 * dt

            # make the particle move
            p[0] += 500 * math.cos(p[2]) * dt # particles X cord
            p[1] += 500 * math.sin(p[2]) * dt # particles Y cord

            # draw the particle
            pygame.draw.circle(surface, color, (int(p[0]),int(p[1])), p[4])
            if p[3] <= 1:
                self.mExplosionsList.remove(p)


    def create(self):
        x = self.mX
        y = self.mY
        number = random.randint(-20,20)
        angle = math.radians(self.mAngle + number)
        size = random.randint(3,7)

        particle = [x,y,angle,255,size]
        self.mParticleList.append(particle)

    def render(self, dt, surface):
        for p in self.mParticleList:
            # adjust color
            color = blast.get_at((int(p[3]), 0))
            p[3] -= 300 * dt

            # make the particle move
            p[0] += 500 * math.cos(p[2]) * dt # particles X cord
            p[1] += 500 * math.sin(p[2]) * dt # particles Y cord

            # draw the particle
            pygame.draw.circle(surface, color, (int(p[0]),int(p[1])), p[4])
            if p[3] <= 1:
                self.mParticleList.remove(p)

class bullet(object):

    def __init__(self):
        self.bulletsList = []

    def create(self, x ,y ,rotation):
        bullet = [x, y, rotation]
        self.bulletsList.append(bullet)

    def update(self, deltaTime, surf):


        # moves the bullets
        for bullet in self.bulletsList:
            rad = math.radians(bullet[2])
            bullet[0] += 1000 * math.cos(rad) * deltaTime
            bullet[1] -= 1000 * math.sin(rad) * deltaTime

        # renders the bullet
            if len(self.bulletsList) >= 1:
                pygame.draw.circle(surf, (255,0,0), (int(bullet[0]),int(bullet[1])), 15)
            if (bullet[0] > 4000 or bullet[0] < 0) or (bullet[1] < 0 or bullet[1] > 4000):
                self.bulletsList.remove(bullet)


    def thingsToHit(self, objectController = None):

        if objectController != None:
            for b in self.bulletsList:
                if objectController.checkForHit(b[0] + 7, b[1] + 7) == True:
                    self.bulletsList.remove(b)

E = emmiter(0,0,0)
B = bullet()

class Ship(object):

    def __init__(self, X, Y):
        self.mX = X
        self.mY = Y
        self.angle = 0
        self.speed = 0
        self.rotShip = pygame.transform.rotate(ship, self.angle)
        self.dealtaTime = 0

    def update(self, deltaTime, areaOfMovement, listOfThingsToHit):
        #area of movement
        maxX = areaOfMovement[2]
        minX = areaOfMovement[0]
        maxY = areaOfMovement[3]
        minY = areaOfMovement[1]

        if self.mX > maxX:
            self.mX = minX + 1
        if self.mX < minX:
            self.mX = maxX - 1
        if self.mY > maxY:
            self.mY = minY + 1
        if self.mY < minY:
            self.mY = maxY - 1
        for x in listOfThingsToHit:
            for b in B.bulletsList:
                if dis(x.mX + 75,x.mY + 75 ,b[0],b[1]) < 75 and x.size == 3:
                    E.createExplosion(b[0],b[1])
                    B.bulletsList.remove(b)
                    x.mDead = True

                    z = x.mX
                    y = x.mY
                    angle = random.uniform(0, math.pi + math.pi)
                    angle2 = random.uniform(0, math.pi + math.pi)
                    speed = random.randint(10, 30)
                    color = random.choice(("b", "s", "t"))
                    a = asteroid.Asteroid( z, y, angle, speed, 0, 0, color, 2)
                    g = asteroid.Asteroid( z, y, angle2, speed, 0, 0, color, 2)
                    listOfThingsToHit.append(a)
                    listOfThingsToHit.append(g)



                if dis(x.mX + 50,x.mY + 50 ,b[0],b[1]) < 50 and x.size == 2:
                    E.createExplosion(b[0],b[1])
                    B.bulletsList.remove(b)
                    x.mDead = True

                    z = x.mX
                    y = x.mY
                    angle = random.uniform(0, math.pi + math.pi)
                    angle2 = random.uniform(0, math.pi + math.pi)
                    speed = random.randint(10, 30)
                    color = random.choice(("b", "s", "t"))
                    a = asteroid.Asteroid( z, y, angle, speed, 0, 0, color, 1)
                    g = asteroid.Asteroid( z, y, angle2, speed, 0, 0, color, 1)
                    listOfThingsToHit.append(a)
                    listOfThingsToHit.append(g)

                if dis(x.mX + 25,x.mY + 25 ,b[0],b[1]) < 25 and x.size == 1:
                    E.createExplosion(b[0],b[1])
                    B.bulletsList.remove(b)
                    x.mDead = True


        #movement and such
        self.deltaTime = deltaTime
        rad = math.radians(self.angle)
        self.mX += self.speed * math.cos(rad) * deltaTime
        self.mY -= self.speed * math.sin(rad) * deltaTime
        self.rotShip = pygame.transform.rotate(ship, self.angle)
        E.updateAngle(-self.angle - 180)
        E.mX = self.mX #+ (self.rotShip.get_width() /2)
        E.mY = self.mY #+ (self.rotShip.get_height()/2)
        if self.speed > 0:
            E.create()
            self.speed -= 150 * deltaTime
            if self.speed <= 0:
                self.speed = 0


    def rotate(self, direction, deltaTime):

        if direction == 1:
            self.angle += 200 * deltaTime
        if direction == -1:
            self.angle -= 200 * deltaTime
        if self.angle >= 360:
            self.angle = 0

    def applyAcceleration(self, direction, dt):
        if direction == 1:
            self.speed += 450 * dt
            if self.speed >= 300:
                self.speed = 300
        if direction == -1:
            self.speed -= 500 * dt
            if self.speed <= 0:
                self.speed = 0

            self.speed -= 150 * dt
            if self.speed <= 0:
                self.speed = 0

    def fire(self, X, Y):
        B.create(self.mX,self.mY, self.angle)

    def render(self, surface):
        a = (self.rotShip.get_width() /2)
        b = (self.rotShip.get_height() /2)
        E.render(self.deltaTime,surface)
        E.renderExplosion(self.deltaTime, surface)
        B.update(self.deltaTime, surface)
        surface.blit(self.rotShip, (self.mX - a, self.mY - b))




