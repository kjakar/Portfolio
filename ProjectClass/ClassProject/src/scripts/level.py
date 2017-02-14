
import pygame

image = pygame.image.load("..\\assets\\images\\level-pic.jpg")
goal = pygame.image.load("..\\assets\\images\\finishline.jpg")

class Level(object):

    def __init__(self,pos, listOfPlayers):
        self.pos = pos
        self.imagePos = pos
        self.goalPos = [-60000+1200,0] # this need to be set to the distance the obstacle spawner is set to and how it's moved needs to be changed
        self.playersList = listOfPlayers
        self.isFinished = False
        self.leaderBoard = []
        self.font = pygame.font.SysFont("Stencil", 45)
        for i in range(4):
            x = [self.playersList[i].name,self.playersList[i].distance]
            self.leaderBoard.append(x)


    def renderLeaderBoard(self, surf):

        #leaderboard sorting =============================

        x = ["empty", 0]
        y = ["empty", 0]
        z = ["empty", 0]
        w = ["empty", 0]
        for player in self.leaderBoard:
            if player[1] > x[1] and player != x:
                x = player
        for player in self.leaderBoard:
            if player[1] > y[1] and player != x:
                y = player
        for player in self.leaderBoard:
            if player[1] > z[1] and player != x and player != y:
                z = player
        for player in self.leaderBoard:
            if player[1] > w[1] and player != x and player != y and player != z:
                w = player

        self.leaderBoard[0] = x
        self.leaderBoard[1] = y
        self.leaderBoard[2] = z
        self.leaderBoard[3] = w

        # drawing Code ============================================

        color1 = (255,255,255)
        color2 = (255,255,255)
        color3 = (255,255,255)
        color4 = (255,255,255)
        line1 = self.font.render(self.leaderBoard[0][0], 1, color1)
        line2 = self.font.render(self.leaderBoard[1][0], 1, color2)
        line3 = self.font.render(self.leaderBoard[2][0], 1, color3)
        line4 = self.font.render(self.leaderBoard[3][0], 1, color4)
        surf.blit(line1,(460, 150))
        surf.blit(line2,(460,250))
        surf.blit(line3,(460,350))
        surf.blit(line4,(460,450))

    def finishLine(self, distance, charPos):
        if charPos >= distance:
            return True
        else:
            return False

    
    def update(self, deltaTime, speed):


        # this changes the players distance ==============
        if self.playersList[0].distance < 100 and self.playersList[1].distance < 100 and self.playersList[2].distance < 100 and self.playersList[3].distance < 100:
            self.pos[0] += deltaTime * speed
            self.goalPos[0] += deltaTime * speed * 2
            self.imagePos[0] += deltaTime * speed
            for player in self.playersList:
                if player.health > 0:
                    player.distance += 1 * deltaTime * player.worldSpeed / 300
                    #if player.distance >= 100:
                    #pygame.surface.fill(0,0,0
        else:
            self.isFinished = True
            for i in range(4):
                x = [self.playersList[i].name,self.playersList[i].distance]
                self.leaderBoard.append(x)


    def render(self, surf):
        global image
        global goal


        # this handles the back ground of the level ======
        w = image.get_width()
        if self.imagePos[0] >= w:
            self.imagePos[0] -= w

        surf.blit(image, self.imagePos)
        surf.blit(image, (self.imagePos[0] - w, self.imagePos[1]))
        surf.blit(goal, (self.goalPos[0], 0))



        #====== progress bar =========================

        pygame.draw.rect(surf, (0,255,0), (192,15,896,25))

        #point1 = [0 + 896 + 172, 0 + 10]   # this is 0%
        #point2 = [40 + 896 + 172, 0 + 10]  # ^
        #point3 = [20 + 896 + 172, 40 + 10] # ^^

        #point1 = [0 + 172, 0 + 10]   # this is 100%
        #point2 = [40 + 172, 0 + 10]  # ^
        #point3 = [20 + 172, 40 + 10] # ^^

        colorList = [(255,0,0),(255,255,20),(0,0,0),(125,0,125)]

        for i in range(len(self.playersList)):
            point1 = [0 + (896 - (896 * self.playersList[i].distance / 100)) + 172, 0]
            point2 = [40 + (896 - (896 * self.playersList[i].distance / 100)) + 172, 0]
            point3 = [20 + (896 - (896 * self.playersList[i].distance / 100)) + 172, 40]
            triangle = [tuple(point1),tuple(point2),tuple(point3)]
            pygame.draw.polygon(surf, colorList[i], triangle)




        

