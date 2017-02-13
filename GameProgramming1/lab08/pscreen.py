import pygame
import time
import random
"""
screen = pygame.display.set_mode((800,600))
deltaTime = 0
clock = pygame.time.Clock()
keyCodes = {}
images = {}"""

# Module (global) variables
screen = None       # The main surface.  Initialized by calling init
images = {}         # All the images we've loaded via loadImage.  Key=String, Value=Surface
keyNames = {}       # A mapping of descriptive names (String) to keycodes (integers)
fonts = {}          # A dictionary of all the fonts we've used thus far.  Key=(String-name, int-font-size).  Value=pygame.Font object
keyList = None      # A list of booleans (one for each key).  Updated by calling update.
deltaTime = 0.0     # The time since the last call to update (or 0.0 for the first time)
clock =  pygame.time.Clock()        # The clock object used to calculate delta-time values
firstUpdate = True  # An internal variable -- used to assign a 0.0 for deltaTime on the first call to update.  This is
                    #    necessary because there may be significant time between init (where we create the clock object)
                    #    and the first call to update.

# every thing commented out is my work
"""
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
"""

def keyInit():

    global keyNames

    keys = pygame.key.get_pressed()
    for i in range(len(keys)):
        keyNames[pygame.key.name(i)] = i
def init(resolution = (800, 600)):
    """
    Initializes pscreen
    :param resolution: the size of the window as a tuple (defaults to 800 x 600)
    :return: None
    """
    global screen
    global clock
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()


def quit():
    """
    Shuts down the pscreen module
    :return: None
    """
    pygame.mixer.quit()
    pygame.font.quit()
    pygame.display.quit()


def update():
    """
    Processes input for this application and update the clock.  This method must be called (exactly) once per frame.
    :return: True if the quit button was pressed, False if not
    """
    global keyList
    global deltaTime
    global clock
    global firstUpdate
    #event = pygame.event.poll()
    keyList = pygame.key.get_pressed()
    deltaTime = clock.tick() / 1000.0
    if firstUpdate:
        deltaTime = 0.0
        firstUpdate = False
    # return event.type == pygame.QUIT


def isKeyDown(keyName):
    """
    Returns True if the given key is down.  See http://www.pygame.org/docs/ref/key.html#pygame.key.name for a list of names
    :param keyName: a string indicating what key we're interested in.
    :return: True if that key is currently down.
    """
    return keyList[keyNames[keyName]]


def getMousePosition():
    """
    :return: a tuple of the mouse's current position
    """
    return pygame.mouse.get_pos()


def isMouseButtonDown(buttonName):
    """
    :param buttonName: 'left', 'middle', or 'right'
    :return: True if that button is currently being pressed
    """
    if buttonName == "left":
        index = 0
    elif buttonName == "middle":
        index = 1
    elif buttonName == "right":
        index = 2
    return pygame.mouse.get_pressed()[index]


def loadImage(name, fileName, section=None):
    """
    Loads an image into pscreen.
    :param name: A descriptive name for this image (used in calls to drawImage)
    :param fileName: The (possibly relative / absolute) path name for the image file to load
    :param section: if None, use the whole image.  If not, extract this rectangular (x, y, w, h)
                    area of the given image.
    :return: The image just loaded into memory.
    """
    global images
    img = pygame.image.load(fileName)
    if section != None:
        surf = pygame.Surface(section[2:])
        surf.blit(img, (0,0), section)
        images[name] = surf
        return surf
    else:
        images[name] = img
        return img



def doBlit(destSurf, srcSurf, x, y, valign, halign):
    """
    This is an internal "helper" function -- it's meant to be called by other functions (like drawImage or drawText)
    """
    dx = 0
    dy = 0
    if halign == "left":
        dx = x
    elif halign == "right":
        dx = x - srcSurf.get_width()
    elif halign == "center":
        dx = x - srcSurf.get_width() // 2

    if valign == "top":
        dy = y
    elif valign == "center":
        dy = y - srcSurf.get_height() // 2
    elif valign == "bottom":
        dy = y - srcSurf.get_height()

    destSurf.blit(srcSurf, (dx, dy))



def drawImage(name, x, y, halign="center", valign="center", destSurf = None):
    """
    Draws this image to the screen (or an off-screen surface)
    :param name: The descriptive name used in a previous call to loadImage
    :param x: The anchor x-position
    :param y: The anchor y-position
    :param halign: "left" => x is the left side of the image on the destination surface
                   "center" => x is the middle of the image on the destination surface
                   "right" => x is the right edge of the image on the destination surface
    :param valign: "top" => y is the top side of the image on the destination surface
                   "center" => y is the middle of the image on the destination surface
                   "bottom" => y is the bottom side of the image on the destination surface
    :param destSurf: if None, draw to the screen.  If given, this is an off-screen surface to draw to.
    :return: None
    """
    global images
    global screen
    img = images[name]
    if destSurf == None:
        destSurf = screen
    doBlit(destSurf, img, x, y, valign, halign)



def drawText(fontName, size, text, x, y, color, halign="center", valign="center", backgroundColor=None, destSurf=None, antiAlias=False):
    """
    This method draws text to a surface
    :param fontName: The string name of a system font.
    :param size: The size of the font (in pixels)
    :param text: The text to draw
    :param x: The x-position of the "anchor" point (the meaning of the anchor is defined by halign and valign)
    :param y: The y-position of the "anchor" point (the meaning of the anchor is defined by halign and valign)
    :param color: The pygame color to draw the text
    :param halign: "left" => x is the left side of the image on the destination surface
                   "center" => x is the middle of the image on the destination surface
                   "right" => x is the right edge of the image on the destination surface
    :param valign: "top" => y is the top side of the image on the destination surface
                   "center" => y is the middle of the image on the destination surface
                   "bottom" => y is the bottom side of the image on the destination surface
    :param backgroundColor: The background color of the text (don't pass a value for transparency)
    :param destSurf: The surface to draw to (if None is passed, draw to the screen)
    :param antiAlias: Do ant-aliasing (defaults to False)
    :return: The surface generated to draw the text.
    """
    global fonts
    global screen
    if (fontName, size) in fonts:
        font = fonts[(fontName, size)]
    else:
        font = pygame.font.SysFont(fontName, size)
        fonts[(fontName, size)] = font
    tempSurf = font.render(text, antiAlias, color, backgroundColor)
    if destSurf == None:
        destSurf = screen
    doBlit(destSurf, tempSurf, x, y, valign, halign)
    return tempSurf




