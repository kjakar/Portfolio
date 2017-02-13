__author__ = 'Alex Jones'

# Everything we do is in degrees and gets converted if need be
#
#
#
#
#









import pygame
import ship
import emitter
import asteroid
import bullet
import pscreen
import math
import random


pygame.display.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Only Poor People use Change")
pscreen.keyInit()

# Vars =================================================================================

gameOver = False
dt = 0
mpos = 0
timer = 0
# funstions ==========================================================================

def spawn(asteroid):
    list1 = random.randint(1,10)

    if list1 == 1:
        list = [- 200, 400, 0]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 2:
        list = [-200, -100, -45]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 3:
        list = [-200, 868, 45]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 4:
        list = [341, -200, -60]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 5:
        list = [682, - 200, -110]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 6:
        list = [1566, -200, -140]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 7:
        list = [341, 968, 60]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 8:
        list = [682, 968, 110]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 9:
        list = [1566, 968, 140]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)
    if list1 == 10:
        list = [1566, 400, 180]
        x = list[0]
        y = list[1]
        state = random.choice((3,3,3,3,3,3,3,2,2,3,3,3))
        direction = list[2]
        print(x,y,state,direction, "hi", list)
        asteroid.create( x ,y , state, direction)


E = emitter.emitter(700, 350, 180)
Asteroid = asteroid.asteroid(0.5)
ship = ship.ship(500,500)
bullet = bullet.bullet()

"""
Asteroid.create(100,100,3,0)
Asteroid.create(300,100,3,0)
Asteroid.create(400,100,3,0)"""

spawn(Asteroid)
while not gameOver:
    #+++++++++++++++
    #+ Update Code +=======================================================================
    #+++++++++++++++

    gameOver = pscreen.update()
    dt = pscreen.deltaTime
    timer += dt
    if timer > 0.5:
        timer = 0
        spawn(Asteroid)
    mpos = pygame.mouse.get_pos()
    ship.move(dt, E)
    bullet.thingsToHit(Asteroid)
    #spawn(asteroid)

    #@@@@@@@@@@@@@@
    #@ User Input @=======================================================================
    #@@@@@@@@@@@@@@



    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        ship.fire(bullet)

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        gameOver = True

    elif event.type == pygame.QUIT:
        gameOver = True
        continue





    if pscreen.isKeyDown(("w")) == True or pscreen.isKeyDown(("up")) == True:
        E.create()
        ship.speedUp(True, dt)
    else:
        ship.speedUp(False, dt)

    if pscreen.isKeyDown(("s")) == True or pscreen.isKeyDown(("down")) == True:
        pass

    if pscreen.isKeyDown(("a")) == True or pscreen.isKeyDown(("left")) == True:
        ship.turn(dt, 1, E)

    if pscreen.isKeyDown(("d")) == True or pscreen.isKeyDown(("right")) == True:
        ship.turn(dt, -1, E)
    if pscreen.isMouseButtonDown("left") == True:
        E.createExplosion(mpos[0], mpos[1])



    #++++++++++++++++
    #+ drawing code +=======================================================================
    #++++++++++++++++

    screen.fill((0,0,0))
    asteroid.E.renderExplosion(dt, screen)
    bullet.update(dt, screen)
    E.render(dt, screen)
    E.renderExplosion(dt, screen)
    Asteroid.render(dt, screen)
    ship.render(screen)

    pygame.display.flip()





































#====================================================================================
# End Stuff =========================================================================
#=====================================================================================
pygame.display.quit()
pygame.font.quit()
pygame.mixer.quit()



