import pygame
import time
import random
screen = pygame.display.set_mode((800,600))
deltaTime = 0
clock = pygame.time.Clock()
keyCodes = {}
images = {}

def loadImage(name, fileName, section = None):
    global images

    x = pygame.image.load(fileName)
    w = x.get_width()
    h = x.get_height()
    y = pygame.image.tostring(x, 'RGB')
    image = (y, section, w, h)

    images[name] = image

def drawImage(name, x, y, halign = "left", valign = "top", destSurf = screen):
    global images

    w = images[name][2]
    h = images[name][3]
    z = pygame.image.fromstring(images[name][0], (w,h), 'RGB')

    if halign == "left" and valign == "top":
        destSurf.blit(z, (x,y), images[name][1])
    if halign == "middle" and valign == "top":
        destSurf.blit(z, (x - int(0.5 * w),y), images[name][1])
    if halign == "right" and valign == "top":
        destSurf.blit(z, (x - w,y), images[name][1])

    if halign == "left" and valign == "middle":
        destSurf.blit(z, (x,y - int(0.5 * h)), images[name][1])
    if halign == "middle" and valign == "middle":
        destSurf.blit(z, (x - int(0.5 * w),y - int(0.5 * h)), images[name][1])
    if halign == "right" and valign == "middle":
        destSurf.blit(z, (x - w,y - int(0.5 * h)), images[name][1])

    if halign == "left" and valign == "bottom":
        destSurf.blit(z, (x,y - h), images[name][1])
    if halign == "middle" and valign == "bottom":
        destSurf.blit(z, (x - int(0.5 * w),y - h), images[name][1])
    if halign == "right" and valign == "bottom":
        destSurf.blit(z, (x - w,y - h), images[name][1])

def isMouseButtonDown(button):

    mouseButtons = pygame.mouse.get_pressed()

    if button == "left" and mouseButtons[0] == True:
        return True

    if button == "middle" and mouseButtons[1] == True:
        return True

    if button == "right" and mouseButtons[2] == True:
        return True

    return False

def getMousePosition():

    mpos = pygame.mouse.get_pos()
    return (mpos)

def isKeyDown(keyName):
    global keyCodes
    allKeys = pygame.key.get_pressed()

    if allKeys[keyCodes[keyName]]:
        return True
    else:
        return False

def update():
    global deltaTime

    deltaTime = clock.tick() / 1000.00

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        return True
    else:
        return False

def init(size = (800, 600)):

    global screen
    global keyCodes

    pygame.mixer.init()
    pygame.display.init()
    pygame.font.init()
    x = size
    screen = pygame.display.set_mode(x)

    allKeys = pygame.key.get_pressed()

    for key in range(0, len(allKeys)):
        i = pygame.key.name(key)
        keyCodes[i] = key



def quit():

    pygame.display.quit()
    pygame.font.quit()
    pygame.mixer.quit()

def drawText (fontName, size, text, x, y, color, halign = "left", valign = "top", backgroundColor = None, destSurf = screen, antiAlias = True):

    font = pygame.font.SysFont(fontName, size)
    fontText = font.render(text, antiAlias, color, backgroundColor)
    wi = fontText.get_width()
    hi = fontText.get_height()
    w = wi
    h = hi
    screen = destSurf

    if halign == "left" and valign == "top":
        screen.blit(fontText, (x,y))
    if halign == "middle" and valign == "top":
        screen.blit(fontText, (x - int(0.5 * w),y))
    if halign == "right" and valign == "top":
        screen.blit(fontText, (x - w,y))

    if halign == "left" and valign == "middle":
        screen.blit(fontText, (x,y - int(0.5 * h)))
    if halign == "middle" and valign == "middle":
        screen.blit(fontText, (x - int(0.5 * w),y - int(0.5 * h)))
    if halign == "right" and valign == "middle":
        screen.blit(fontText, (x - w,y - int(0.5 * h)))

    if halign == "left" and valign == "bottom":
        screen.blit(fontText, (x,y - h))
    if halign == "middle" and valign == "bottom":
        screen.blit(fontText, (x - int(0.5 * w),y - h))
    if halign == "right" and valign == "bottom":
        screen.blit(fontText, (x - w,y - h))
