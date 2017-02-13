__author__ = 'Alex Jones'

import pygame
import time
import random

# <editor-fold desc="Setup-Code">

pygame.display.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((600,1000))
pygame.display.set_caption("We come in peace!")
font = pygame.font.SysFont("Times New Roman", 24)
#Images=====
ship = pygame.image.load("player.png") #128x64
marsSmall = pygame.image.load("mars.png")
mars = pygame.transform.scale(marsSmall, (1000,1000))
enemySmall = pygame.image.load("ships.png")
AI = pygame.transform.scale(enemySmall, (1280, 1280))
galaxyBIG = pygame.image.load("galaxy.jpg")
galaxySide = pygame.transform.scale(galaxyBIG, (1530, 600))
galaxy = pygame.transform.rotate(galaxySide, 90)
start = pygame.image.load("start.png")
options = pygame.image.load("options.png")
quit = pygame.image.load("quit.png")
MSoriginal = pygame.image.load("motehrShip.png")
#Sounds=====
pygame.mixer.music.load("laserCannon.wav")
pygame.mixer.music.load("laser.wav")
pygame.mixer.music.load("Kaboom.wav")
pygame.mixer.music.load("Splooge.wav")
laser = pygame.mixer.Sound("laser.wav")
explosion = pygame.mixer.Sound("Kaboom.wav")
scream = pygame.mixer.Sound("Splooge.wav")
cannon = pygame.mixer.Sound("laserCannon.wav")
# </editor-fold>

# <editor-fold desc="Global Vars">
#Global-Vars===========================================================

gameOver = False
mpos = pygame.mouse.get_pos()
clock = pygame.time.Clock()
spawnTimer = 0.0
shotTimer = 0.0
laserCannonTimer = 0.0
levelTimer = 0.0
lives = 4
level = 0
score = 0
HP = 100
# </editor-fold>

# <editor-fold desc="Functions">
#Functions=============================================================

def dis(x1, y1, x2, y2):
    dis = (((x2 -x1)** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dis
# </editor-fold>

# <editor-fold desc="Game Vars">
#Game-vars=============================================================

stars = [[100,50],[737,100],[432,150],[12,200],[397,250],[516,300],[627,350],[183,400],[246,450],[813,500],[0,550],[300,150],[937,200],[632,250],[212,300],[597,350],[716,400],[827,450],[383,500],[446,550],[13,20],[200,80]]  # x = 1000, y = 600
shipXY = [266,800]
bullets = []
Ebullets =[]
laserCannon =[]
enemy = []
MSXY = [10,-300]
MSMove = 1
# </editor-fold>

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#=====================         Start Menu      ===========================#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
while gameOver == False and level == 0:

    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True

    elif event.type == pygame.QUIT:
        gameOver = True
        continue

    mpos = pygame.mouse.get_pos()

    screen.blit(galaxy, (0,0))
    screen.blit(start, (100, 200))
    screen.blit(options, (100, 450))
    screen.blit(quit, (100, 700))
    pygame.display.flip()

    mouseButtons = pygame.mouse.get_pressed()
    if mouseButtons[0] and mpos[0] >= 100 and mpos[0] <= 500 and mpos[1] >= 200 and mpos[1] <400:
        level = 1
        print("LETS DO THIS!")
        continue
    if mouseButtons[0] and mpos[0] >= 100 and mpos[0] <= 500 and mpos[1] >= 450 and mpos[1] <650:
        print("This does nothing sorry")
    if mouseButtons[0] and mpos[0] >= 100 and mpos[0] <= 500 and mpos[1] >= 700 and mpos[1] <900:
        gameOver = True
        continue

#time.sleep(7) #this is here so that all of the objects in level one will not start before loading in.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#==============                 level one   ==============================#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#Game-Code=============================================================

while gameOver == False and level == 1:
    dt = clock.tick()/1000.0
    spawnTimer += dt
    shotTimer +=dt
#User-Input============================================================
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_w]:
        shipXY[1] -= 200 * dt
    if allKeys[pygame.K_a]:
        shipXY[0] -= 200 * dt
    if allKeys[pygame.K_s]:
        shipXY[1] += 200 * dt
    if allKeys[pygame.K_d]:
        shipXY[0] += 200 * dt

    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True
        continue

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and shotTimer > 1.0:
        x = shipXY[0] + 31
        y = shipXY[1]
        x2 = shipXY[0] + 31
        y2 = shipXY[1] + 10
        shot = [x,y,x2,y2]
        bullets.append(shot)
        laser.play()
        shotTimer = 0.0

    elif event.type == pygame.QUIT:
        gameOver = True
        continue
#Update-Code===========================================================
    if spawnTimer >= 2.5:
        x = random.randint(0, 536)
        y = -84
        row = random.randint(1,20) * 64 - 64
        column = random.randint(1,20) * 64 - 64
        it = [x,y,row,column]
        enemy.append(it)
        spawnTimer = 0.0

    for s in stars:
        if s[0] >= 1000:
            s[0] = 0
        s[0] += 10 * dt
    if shipXY[0] <= 0:
        shipXY[0] = 1
    if shipXY[0] >= 539:
        shipXY[0] = 538
    if shipXY[1] <= 0:
        shipXY[1] = 1
    if shipXY[1] >= 937:
        shipXY[1] = 936

    for shot in bullets:
        for it in enemy:

            if dis(shot[0],shot[1],it[0] + 34,it[1] +34) <= 34:
                bullets.remove(shot)
                enemy.remove(it)
                explosion.play()
                score += 1
    for it in enemy:
        go = random.randint(1,1000)
        if go == 20:
            x = it[0] + 31
            y = it[1]
            x2 = it[0] + 31
            y2 = it[1] + 10
            Eshot = [x,y,x2,y2]
            Ebullets.append(Eshot)
            laser.play()
    for Eshot in Ebullets:
        if dis(Eshot[0],Eshot[1],shipXY[0] + 34,shipXY[1] +34) <= 34:
                Ebullets.remove(Eshot)
                lives -= 1
                explosion.play()
    for it in enemy:
        if it[1] >= 1010:
            enemy.remove(it)
            lives -= 1
            scream.play()
    if score >= 25:
        lives = 4
        level = 2
        score = 0
        print("level 2")
        continue
    if lives == 0:
        s = pygame.Surface((600,1000), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,0,0,178))                         # notice the alpha value in the color
        screen.blit(s, (0,0))
        LossText = font.render(("YOU LOSE"), True, (0,255,0))
        screen.blit(LossText, (260,400))
        pygame.display.flip()
        time.sleep(5)
        gameOver =True
        continue
#drawing code/EndStuff

    screen.fill((0,0,0))


    for star in stars:
        # Draw the current bubble
        x = star[1]
        y = star[0]
        radius = random.randint(3,4) #this makes the stars sparkle :)
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), radius)

    screen.blit(mars, (-200,650))

    for shot in bullets:
        shot[1] -= 300 * dt
        shot[3] -= 300 * dt
        pygame.draw.line(screen, (255,0,0), (int(shot[0]),int(shot[1])), (int(shot[2]), int(shot[3])), 5)
        if shot[3] < 0:
            bullets.remove(shot)
    for Eshot in Ebullets:
        Eshot[1] += 300 * dt
        Eshot[3] += 300 * dt
        pygame.draw.line(screen, (0,0,255), (int(Eshot[0]),int(Eshot[1])), (int(Eshot[2]), int(Eshot[3])), 5)
        if Eshot[3] > 1000:
            Ebullets.remove(Eshot)
    for it in enemy:
        it[1] += 130 * dt
        screen.blit(AI, (it[0], it[1]), (it[2], it[3],64,64))
    screen.blit(ship, (int(shipXY[0]),int(shipXY[1])), (0,0,64,64))
    mpos = pygame.mouse.get_pos()
    ScoreText = font.render(("Score: " + str(score)), True, (0, 255, 0))
    LivesText = font.render(("Lives Left: " + str(lives)), True, (0,255,0))
    screen.blit(ScoreText, (0,0))
    screen.blit(LivesText, (0,30))
    pygame.display .flip()
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#==============                 level two   ==============================#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

#Game-Code=============================================================

while gameOver == False and level == 2:
    dt = clock.tick()/1000.0
    spawnTimer += dt
    shotTimer +=dt
#User-Input============================================================
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_w]:
        shipXY[1] -= 150 * dt
    if allKeys[pygame.K_a]:
        shipXY[0] -= 150 * dt
    if allKeys[pygame.K_s]:
        shipXY[1] += 150 * dt
    if allKeys[pygame.K_d]:
        shipXY[0] += 150 * dt

    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True
        continue

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and shotTimer > 1.0:
        x = shipXY[0] + 31
        y = shipXY[1]
        x2 = shipXY[0] + 31
        y2 = shipXY[1] + 10
        shot = [x,y,x2,y2]
        bullets.append(shot)
        laser.play()
        shotTimer = 0.0

    elif event.type == pygame.QUIT:
        gameOver = True
        continue
#Update-Code===========================================================
    if spawnTimer >= 2.5:
        x = random.randint(0, 536)
        y = -84
        row = random.randint(1,20) * 64 - 64
        column = random.randint(1,20) * 64 - 64
        it = [x,y,row,column]
        enemy.append(it)
        spawnTimer = 0.0

    for s in stars:
        if s[0] >= 1000:
            s[0] = 0
        s[0] += 10 * dt
    if shipXY[0] <= 0:
        shipXY[0] = 1
    if shipXY[0] >= 539:
        shipXY[0] = 538
    if shipXY[1] <= 0:
        shipXY[1] = 1
    if shipXY[1] >= 937:
        shipXY[1] = 936

    for shot in bullets:
        for it in enemy:

            if dis(shot[0],shot[1],it[0] + 34,it[1] +34) <= 34:
                bullets.remove(shot)
                enemy.remove(it)
                explosion.play()
                score += 1
    for it in enemy:
        go = random.randint(1,500)
        if go == 20:
            x = it[0] + 31
            y = it[1]
            x2 = it[0] + 31
            y2 = it[1] + 10
            Eshot = [x,y,x2,y2]
            Ebullets.append(Eshot)
            laser.play()
    for Eshot in Ebullets:
        if dis(Eshot[0],Eshot[1],shipXY[0] + 34,shipXY[1] +34) <= 34:
                Ebullets.remove(Eshot)
                lives -= 1
                explosion.play()
    for it in enemy:
        if it[1] >= 1010:
            enemy.remove(it)
            lives -= 1
            scream.play()
    if score >= 25:
        lives = 5
        level = 3
        continue
    if lives == 0:
        s = pygame.Surface((600,1000), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,0,0,178))                         # notice the alpha value in the color
        screen.blit(s, (0,0))
        LossText = font.render(("YOU LOSE"), True, (0,255,0))
        screen.blit(LossText, (260,400))
        pygame.display.flip()
        time.sleep(5)
        gameOver =True
        continue
#drawing code/EndStuff

    screen.fill((0,0,0))


    for star in stars:
        x = star[1]
        y = star[0]
        radius = random.randint(3,4) #this makes the stars sparkle :)
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), radius)

    screen.blit(mars, (-200,650))

    for shot in bullets:
        shot[1] -= 300 * dt
        shot[3] -= 300 * dt
        pygame.draw.line(screen, (255,0,0), (int(shot[0]),int(shot[1])), (int(shot[2]), int(shot[3])), 5)
        if shot[3] < 0:
            bullets.remove(shot)
    for Eshot in Ebullets:
        Eshot[1] += 300 * dt
        Eshot[3] += 300 * dt
        pygame.draw.line(screen, (0,0,255), (int(Eshot[0]),int(Eshot[1])), (int(Eshot[2]), int(Eshot[3])), 5)
        if Eshot[3] > 1000:
            Ebullets.remove(Eshot)
    for it in enemy:
        it[1] += 180 * dt
        screen.blit(AI, (it[0], it[1]), (it[2], it[3],64,64))
    screen.blit(ship, (int(shipXY[0]),int(shipXY[1])), (0,0,64,64))
    mpos = pygame.mouse.get_pos()
    ScoreText = font.render(("Score: " + str(score)), True, (0, 255, 0))
    LivesText = font.render(("Lives Left: " + str(lives)), True, (0,255,0))
    screen.blit(ScoreText, (0,0))
    screen.blit(LivesText, (0,30))
    pygame.display .flip()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#==============                 level three   ============================#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#Game-Code=============================================================

while gameOver == False and level == 3:
    dt = clock.tick()/1000.0
    spawnTimer += dt
    shotTimer +=dt
#User-Input============================================================
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_w]:
        shipXY[1] -= 350 * dt
    if allKeys[pygame.K_a]:
        shipXY[0] -= 350 * dt
    if allKeys[pygame.K_s]:
        shipXY[1] += 350 * dt
    if allKeys[pygame.K_d]:
        shipXY[0] += 350 * dt

    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True
        continue

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and shotTimer > 1.0:
        x = shipXY[0] + 31
        y = shipXY[1]
        x2 = shipXY[0] + 31
        y2 = shipXY[1] + 10
        shot = [x,y,x2,y2]
        bullets.append(shot)
        laser.play()
        shotTimer = 0.0

    elif event.type == pygame.QUIT:
        gameOver = True
        continue
#Update-Code===========================================================
    if spawnTimer >= 1.5:
        x = random.randint(0, 536)
        y = -84
        row = random.randint(1,20) * 64 - 64
        column = random.randint(1,20) * 64 - 64
        it = [x,y,row,column]
        enemy.append(it)
        spawnTimer = 0.0

    for s in stars:
        if s[0] >= 1000:
            s[0] = 0
        s[0] += 10 * dt
    if shipXY[0] <= 0:
        shipXY[0] = 1
    if shipXY[0] >= 539:
        shipXY[0] = 538
    if shipXY[1] <= 0:
        shipXY[1] = 1
    if shipXY[1] >= 937:
        shipXY[1] = 936

    for shot in bullets:
        for it in enemy:

            if dis(shot[0],shot[1],it[0] + 34,it[1] +34) <= 34:
                bullets.remove(shot)
                enemy.remove(it)
                explosion.play()
                score += 1
    for it in enemy:
        go = random.randint(1,400)
        if go == 20:
            x = it[0] + 31
            y = it[1]
            x2 = it[0] + 31
            y2 = it[1] + 10
            Eshot = [x,y,x2,y2]
            Ebullets.append(Eshot)
            laser.play()
    for Eshot in Ebullets:
        if dis(Eshot[0],Eshot[1],shipXY[0] + 34,shipXY[1] +34) <= 34:
                Ebullets.remove(Eshot)
                lives -= 1
                explosion.play()
    for it in enemy:
        if it[1] >= 1010:
            enemy.remove(it)
            lives -= 1
            scream.play()
    if score >= 25:
        score = 0
        lives = 6
        level = 4
        continue
    if lives == 0:
        s = pygame.Surface((600,1000), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,0,0,178))                         # notice the alpha value in the color
        screen.blit(s, (0,0))
        LossText = font.render(("YOU LOSE"), True, (0,255,0))
        screen.blit(LossText, (260,400))
        pygame.display.flip()
        time.sleep(5)
        gameOver =True
        continue
#drawing code/EndStuff

    screen.fill((0,0,0))


    for star in stars:
        x = star[1]
        y = star[0]
        radius = random.randint(3,4) #this makes the stars sparkle :)
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), radius)
    screen.blit(mars, (-200,650))
    for shot in bullets:
        shot[1] -= 300 * dt
        shot[3] -= 300 * dt
        pygame.draw.line(screen, (255,0,0), (int(shot[0]),int(shot[1])), (int(shot[2]), int(shot[3])), 5)
        if shot[3] < 0:
            bullets.remove(shot)
    for Eshot in Ebullets:
        Eshot[1] += 450 * dt
        Eshot[3] += 450 * dt
        pygame.draw.line(screen, (0,0,255), (int(Eshot[0]),int(Eshot[1])), (int(Eshot[2]), int(Eshot[3])), 5)
        if Eshot[3] > 1000:
            Ebullets.remove(Eshot)
    for it in enemy:
        it[1] += 200 * dt
        screen.blit(AI, (it[0], it[1]), (it[2], it[3],64,64))
    screen.blit(ship, (int(shipXY[0]),int(shipXY[1])), (0,0,64,64))
    mpos = pygame.mouse.get_pos()
    ScoreText = font.render(("Score: " + str(score)), True, (0, 255, 0))
    LivesText = font.render(("Lives Left: " + str(lives)), True, (0,255,0))
    screen.blit(ScoreText, (0,0))
    screen.blit(LivesText, (0,30))
    pygame.display .flip()

"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#==============                 FINAL LEVEL          =====================#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

#Game-Code=============================================================

while gameOver == False and level == 4:
    dt = clock.tick()/1000.0
    spawnTimer += dt
    shotTimer +=dt
    levelTimer += dt

#User-Input============================================================
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_w]:
        shipXY[1] -= 300 * dt
    if allKeys[pygame.K_a]:
        shipXY[0] -= 300 * dt
    if allKeys[pygame.K_s]:
        shipXY[1] += 300 * dt
    if allKeys[pygame.K_d]:
        shipXY[0] += 300 * dt

    event = pygame.event.poll()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True
        continue

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and shotTimer > 0.25:
        x = shipXY[0] + 31
        y = shipXY[1]
        x2 = shipXY[0] + 31
        y2 = shipXY[1] + 10
        shot = [x,y,x2,y2]
        bullets.append(shot)
        laser.play()
        shotTimer = 0.0

    elif event.type == pygame.QUIT:
        gameOver = True
        continue
#Update-Code===========================================================
    if levelTimer >= 15.0:
        MSXY[0] -= 50 * dt * MSMove
    if levelTimer >16.5:
        cannon.play()
    if levelTimer >= 17.5:
        x = MSXY[0] + 97
        y = MSXY[1] + 30
        x2 = MSXY[0] + 97
        y2 = MSXY[1] + 1000
        Eshot = [x,y,x2,y2]
        laserCannon.append(Eshot)
        laser.play()
        if shipXY [0] + 32 >= MSXY[0] + 77 and shipXY [0] <= MSXY[0] + 117:
            lives -= 1

    if levelTimer >= 19:
        for Eshot in laserCannon:
            laserCannon.remove(Eshot)
        levelTimer = 0.0

    if MSXY[1] <= 100:
        MSXY[1] += 30 * dt
    if MSXY[0] <= 0 or MSXY[0] >= 406:
        MSMove = -MSMove
    MSXY[0] += 50 * dt * MSMove
    for s in stars:
        if s[0] >= 1000:
            s[0] = 0
        s[0] += 10 * dt
    if shipXY[0] <= 0:
        shipXY[0] = 1
    if shipXY[0] >= 539:
        shipXY[0] = 538
    if shipXY[1] <= 0:
        shipXY[1] = 1
    if shipXY[1] >= 937:
        shipXY[1] = 936

    for shot in bullets:

        if dis(shot[0],shot[1],MSXY[0] + 97,MSXY[1] +51) <= 25:
            bullets.remove(shot)
            explosion.play()
            HP -= 1

    #this is the left gun
    go = random.randint(1,150)
    if go == 20 and HP >= 1:
        x = MSXY[0] + 31
        y = MSXY[1] + 30
        x2 = MSXY[0] + 31
        y2 = MSXY[1] + 40
        Eshot = [x,y,x2,y2]
        Ebullets.append(Eshot)
        laser.play()
    #this is the right gun
    go2 = random.randint(1,150)
    if go2 == 20 and HP >=1:
        x = MSXY[0] + 163
        y = MSXY[1] + 30
        x2 = MSXY[0] + 163
        y2 = MSXY[1] + 40
        Eshot = [x,y,x2,y2]
        Ebullets.append(Eshot)
        laser.play()

    for Eshot in Ebullets:
        if dis(Eshot[0],Eshot[1],shipXY[0] + 34,shipXY[1] +34) <= 34:
                Ebullets.remove(Eshot)
                lives -= 1
                explosion.play()

    if score >= 25:
        lives = 4
        level = 2
        score = 0
        continue
    if lives == 0:
        s = pygame.Surface((600,1000), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,0,0,178))                         # notice the alpha value in the color
        screen.blit(s, (0,0))
        LossText = font.render(("YOU LOSE"), True, (0,255,0))
        screen.blit(LossText, (260,400))
        pygame.display.flip()
        time.sleep(5)
        gameOver =True
        continue
#drawing code/EndStuff

    screen.fill((0,0,0))


    for star in stars:
        x = star[1]
        y = star[0]
        radius = random.randint(3,4) #this makes the stars sparkle :)
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), radius)

    screen.blit(mars, (-200,650))

    for shot in bullets:
        shot[1] -= 300 * dt
        shot[3] -= 300 * dt
        pygame.draw.line(screen, (255,0,0), (int(shot[0]),int(shot[1])), (int(shot[2]), int(shot[3])), 5)
        if shot[3] < 0:
            bullets.remove(shot)
    for Eshot in Ebullets:
        Eshot[1] += 300 * dt
        Eshot[3] += 300 * dt
        pygame.draw.line(screen, (0,0,255), (int(Eshot[0]),int(Eshot[1])), (int(Eshot[2]), int(Eshot[3])), 5)
        if Eshot[3] > 1000:
            Ebullets.remove(Eshot)
    for Eshot in laserCannon:
        Eshot[1] += 1000 * dt
        Eshot[3] += 1000 * dt
        pygame.draw.line(screen, (0,0,255), (int(Eshot[0]),int(Eshot[1])), (int(Eshot[2]), int(Eshot[3])), 30)
        if Eshot[3] > 1000:
            laserCannon.remove(Eshot)

    if HP >= 1:
        screen.blit(MSoriginal, (int(MSXY[0]),int(MSXY[1])))
    screen.blit(ship, (int(shipXY[0]),int(shipXY[1])), (0,0,64,64))
    mpos = pygame.mouse.get_pos()
    ScoreText = font.render(("Score: " + str(score)), True, (0, 255, 0))
    LivesText = font.render(("Lives Left: " + str(lives)), True, (0,255,0))
    HPText = font.render(("==++ HP ++=="), True, (255,0,0))
    pygame.draw.rect(screen, (255,0,0), (0,5,6 * HP, 15))
    screen.blit(ScoreText, (0,30))
    screen.blit(LivesText, (0,60))
    screen.blit(HPText, (230, 30))
    pygame.display .flip()

#Quit==================================================================

pygame.display.quit()
