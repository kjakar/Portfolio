
# Importing our modules.  You'll write all of them (except for pygame, math and random of course)
import pygame
import ship
import asteroid
import random
import math


########################################
# Pygame startup                       #
########################################
pygame.display.init()
pygame.font.init()
pygame.mixer.init()
win_width = 1366
win_height = 768
screen = pygame.display.set_mode((win_width, win_height))
fontObj = pygame.font.SysFont("Courier New", 12)
pygame.display.set_caption("Only Poor People use Change")
done = False
clock = pygame.time.Clock()

########################################
# Load game assets / objects           #
########################################
credits = ["asteroids sounds / music: http://www.classicgaming.cc/classics/asteroids/sounds.php",
           "spaceship image from http://opengameart.org/content/spaceship-tutorial-0",
           "asteroid image from https://forum.thegamecreators.com/thread/209786"]
asteroidImage = pygame.image.load("images\\asteroids.png")
asteroidGradient = pygame.image.load("images\\explosion_gradient.png")
S = ship.Ship(400, 300)
alist = []
for i in range(15):
    x = random.randint(0, win_width)
    y = random.randint(0, win_height)
    angle = random.uniform(0, math.pi + math.pi)
    speed = random.randint(10, 30)
    color = random.choice(("b", "s", "t"))
    a = asteroid.Asteroid( x, y, angle, speed, asteroidImage, asteroidGradient, color, 3)
    alist.append(a)


########################################
# Game Loop                            #
########################################
while not done:
    # @@@@@@@@@@@@@@
    # @ UPDATE     @
    # @@@@@@@@@@@@@@
    dt = clock.tick() / 1000.0
    S.update(dt, (0,0,win_width,win_height), alist)
    for a in alist:
        a.update(dt, (0, 0, win_width, win_height))
        if a.mDead:
            alist.remove(a)

    # @@@@@@@@@@@@@@
    # @ INPUT      @
    # @@@@@@@@@@@@@@
    # ... event handling
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
        if event.key == pygame.K_SPACE:
            S.fire(0,0)
    # ...device-polling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        S.rotate(1, dt)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        S.rotate(-1, dt)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        S.applyAcceleration(1, dt)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        S.applyAcceleration(-0.4, dt)
    mbut = pygame.mouse.get_pressed()
    if mbut[0]:
        mx, my = pygame.mouse.get_pos()
        S.fire(mx, my)


    # @@@@@@@@@@@@@@
    # @ DRAW       @
    # @@@@@@@@@@@@@@
    screen.fill((0,0,0))
    for a in alist:
        a.render(screen)
    S.render(screen)
    # ... draw the credits (if you use the assets from the web page, keep this in)
    y = win_height
    for c in credits:
        tempS = fontObj.render(c, True, (128,128,128))
        y -= tempS.get_height()
        x = win_width - tempS.get_width()
        screen.blit(tempS, (x, y))
    pygame.display.flip()


########################################
# Pygame shutdown                      #
########################################
pygame.mixer.quit()
pygame.font.quit()
pygame.display.quit()

