__author__ = 'Alex Jones'

import pygame
import time
import random
import level
import player
import obstacle
import ai
import leaderBoard
import menus
import credit
import FakePlayer

#set-up================================================================
pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Album Title Goes Here")
font = pygame.font.SysFont("Times New Roman", 24)
clock = pygame.time.Clock()
dt = clock.tick() / 1000
boost = 1000

#Global-Vars===========================================================
gameOver = False
mpos = pygame.mouse.get_pos()
mode = "mainMenu"
playersList = []
AIList = []
obstacleList = []
clicking = 0.0

# Game Vars ===========================================================

player1 = None

#Functions=============================================================
def spawnObstacles(distance, howFarApart):
    x = distance - 1240
    y = howFarApart
    z = -100
    list = []
    size = ["large","medium","small"]
    pos = ["top","bottom","middle"]
    for i in range(int(x / y)):
        z -= y
        thing = obstacle.obstacle(size[random.randint(0,2)],pos[random.randint(0,2)],z)
        list.append(thing)
    return list
def setup():
    global obstacleList
    global playersList
    global AIList
    global player1
    global creep
    global creep2
    global creep3
    obstacleList = []
    obstacleList = spawnObstacles(60000, 300)
    playersList = []
    player1 = None
    #player1 = player.Player((1000,360), 10) # this is the user
    #playersList.append(player1)
    AIList = []

    # this is all the little sharks that drift in from the front

    for i in range(40):
        x = random.randint(-30000,700)
        y = random.randint(100,600)
        bot = ai.AI( (x,y), 200)
        bot.render(screen,dt) # this is here to set the bots rect : this IS NEEDED
        AIList.append(bot)
        
    # this sets up the ai the player is racing against
    creep = FakePlayer.Bot((100,160), 10, 2, 2, "Sharky McSharkface")
    playersList.append(creep)
    creep2 = FakePlayer.Bot((100,560), 10, 3, 3, "Huge Jaws")
    playersList.append(creep2)
    creep3 = FakePlayer.Bot((100,360), 10, 4, 4, "Jaws Breaker")
    playersList.append(creep3)

#Game-vars=============================================================
 # at current player speeds the level is 20k pixels long
menu = menus.MainMenu()
selectMenu = menus.playerSelect()
overMenu = menus.gameOver()

LB = leaderBoard.LeaderBoard()
gameOverText = font.render("Game Over", 1, (255,255,255))

setup()
player1 = player.Player((1000,360), 10) # this is the user
playersList.append(player1)
map = level.Level([0,0], playersList)


#======================================================================================================================#
#========================                             Game-Code                          ==============================#
#======================================================================================================================#
while gameOver == False:
    dt = clock.tick() / 1000
    count = font.render("Boost:"+str(boost), 1, (0,0,0))
    event = pygame.event.poll()
    click = pygame.mouse.get_pressed()

########################################################################
#####                           MAIN MENU                          #####
########################################################################
    if mode == "mainMenu":   
        menu.update()
        menu.render(screen)
        if click == (1,0,0)and menu.hover== "Single":
            clicking = 1.0
            mode = "playerSelect"


        elif click == (1,0,0) and menu.hover == "Credits":
            mode = "credit"
    if event.type == pygame.QUIT:
            gameOver = True
            continue

########################################################################
#####                         PLAYER SELECT                        #####
########################################################################
    if mode == "playerSelect":
        selectMenu.update()
        selectMenu.render(screen)
        if clicking <= 0:
            if click == (1,0,0)and selectMenu.hover == "1":
                mode = "game"
                player1.changeSprite(menus.smitty)
            if click == (1,0,0)and selectMenu.hover == "2":
                mode = "game"
                player1.changeSprite(menus.legs)
            if click == (1,0,0)and selectMenu.hover == "3":
                mode = "game"
                player1.changeSprite(menus.zombie)
            if click == (1,0,0)and selectMenu.hover == "4":
                mode = "game"
                player1.changeSprite(menus.under)
            if click == (1,0,0)and selectMenu.hover == "5":
                mode = "game"
                player1.changeSprite(menus.pirateShark)
        else:
            clicking -= dt

    if event.type == pygame.QUIT:
            gameOver = True
            continue



########################################################################
#####                       GAME OVER MENU                         #####
########################################################################
    if mode == "gameOver":
        overMenu.update()
        overMenu.render(screen)
        map.renderLeaderBoard(screen)
        if click == (1,0,0)and overMenu.hover== "5":
            clicking = 1.0
            setup()
            player1 = player.Player((1000,360), 10) # this is the user
            playersList.append(player1)
            map = level.Level([0,0], playersList)
            mode = "game"
            
        if click == (1,0,0)and overMenu.hover== "6":
            clicking = 1.0
            setup()
            player1 = player.Player((1000,360), 10) # this is the user
            playersList.append(player1)
            map = level.Level([0,0], playersList)
            mode = "mainMenu"

    if event.type == pygame.QUIT:
            gameOver = True
            continue
        
########################################################################
#####                            GAME                              #####
########################################################################
    if mode == "game":


        # test cases =====================================================

        if map.isFinished:
            mode = "gameOver"
##        player1.health = 5
##        player1.worldSpeed = 10000
        #none right now

        # test cases ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        mpos = pygame.mouse.get_pos()

        if player1.distance >= 100:
            dt = 0

        map.update(dt, player1.worldSpeed)

        for bot in AIList:
            bot.update(dt)

        creep.update(dt, player1)
        creep2.update(dt, player1)
        creep3.update(dt, player1)

        # obstacle vs player hit detection ===============================
        for o in obstacleList:
            o.update(dt, player1.worldSpeed)
            for p in playersList:
                if o.hitDetect(p) and p.invincible <= 0:
                    p.health -= 1
                    p.invincible = 1

        # AI vs player hit detection ======================================
        for bot in AIList:
            for p in playersList:
                if bot.hitDetect(p):
                    if p.health >= bot.health:
                        p.health += 1
                        if bot not in AIList:
                            pass
                        else:
                            AIList.remove(bot)


        event = pygame.event.poll()

        #Once per press ====================================================
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("pressing space")
        if event.type == pygame.QUIT:
            gameOver = True
            continue

        #Held Down Presses ================================================
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            gameOver = True
        if keys[pygame.K_SPACE]:
            #player1.shoot()
            pass
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player1.update(dt,"left")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player1.update(dt,"right")
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player1.update(dt,"up")
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player1.update(dt,"down")
        if keys[pygame.K_t]:
            player1.hardMode = 600
        if keys[pygame.K_SPACE]:
            player1.boost(dt,boost,"boost")
            boost -= 40
            if boost < 0:
                boost = 0
        else:
            player1.isBoost = False
            boost += 4
            if boost >= 1000:
                boost = 1000

    #Drwing Code ==========================================================
        screen.fill((0,0,0))

        map.render(screen)
        for bot in AIList:
            bot.render(screen,dt)

        for o in obstacleList:
            o.render(screen)


        #LB.render(screen, font)
        #screen.blit(count,(0, 690))
        creep.render(screen, dt)
        creep2.render(screen, dt)
        creep3.render(screen, dt)
        player1.render(screen, dt)

    #EndStuff
    
    pygame.display.flip()

########################################################################
#####                           CREDITS                            #####
########################################################################
    if mode == "credit":
        credit.credit(screen,dt)
        mode = "mainMenu"
        if event.type == pygame.QUIT:
            gameOver = True
            continue

"""screen.fill((0,0,0))
screen.blit(gameOverText,(640,360))
LB.render(screen, font)
pygame.display.update()
pygame.time.delay(2000)"""

#Quit==================================================================

pygame.display.quit()
pygame.mixer.quit()
