__author__ = 'Alex Jones'

# player = 3 ai = 2  player2 = 1 empty = 0

import pscreen
import pygame
import random
import time

pscreen.init((480,660))

# Images ========================================================

checkersLarge = pygame.image.load("checkers.png")
checkers = pygame.transform.scale(checkersLarge, (144,72))


#Global Vars=====================================================

gameOver = False
mpos = 0
click = False
pvp = True
turn = 3
coins = []
holes = [(40, 40), (120, 40), (200, 40), (280, 40), (360, 40), (440, 40), (40, 120), (120, 120), (200, 120), (280, 120), (360, 120), (440, 120), (40, 200), (120, 200), (200, 200), (280, 200), (360, 200), (440, 200), (40, 280), (120, 280), (200, 280), (280, 280), (360, 280), (440, 280), (40, 360), (120, 360), (200, 360), (280, 360), (360, 360), (440, 360), (40, 440), (120, 440), (200, 440), (280, 440), (360, 440), (440, 440), (40, 520), (120, 520), (200, 520), (280, 520), (360, 520), (440, 520)]
win = False
timer = 0
MainMenu = True

grid = [0,0,0,0,0,0,\
        0,0,0,0,0,0,\
        0,0,0,0,0,0,\
        0,0,0,0,0,0,\
        0,0,0,0,0,0,\
        0,0,0,0,0,0,\
        0,0,0,0,0,0]

# Functions ================================================================

def checkForWin():
    global win
    i = 21


    while  i <= 41:
        x = i - 7
        y = i - 14
        z = i - 21
        if grid[i] == 3 and grid[x] == 3 and grid[y] == 3 and grid[z] == 3:
            win = True
        i += 1

    j = 18

    while j <= 41:
        x = j - 6
        y = j - 12
        z = j - 18
        if grid[j] == 3 and grid[x] == 3 and grid[y] == 3 and grid[z] == 3:
            win = True
        j += 1

    k = 15

    while k <= 41:
        x = k - 5
        y = k - 10
        z = k - 15
        if grid[k] == 3 and grid[x] == 3 and grid[y] == 3 and grid[z] == 3:
            win = True
        k += 1

    l = 0

    while l <= 38:
        x = l + 1
        y = l + 2
        z = l + 3
        if grid[l] == 3 and grid[x] == 3 and grid[y] == 3 and grid[z] == 3:
            win = True
        l += 1
    # This i for ai
    i = 21


    while  i <= 41:
        x = i - 7
        y = i - 14
        z = i - 21
        if grid[i] == 2 and grid[x] == 2 and grid[y] == 2 and grid[z] == 2:
            win = 2
        i += 1

    j = 18

    while j <= 41:
        x = j - 6
        y = j - 12
        z = j - 18
        if grid[j] == 2 and grid[x] == 2 and grid[y] == 2 and grid[z] == 2:
            win = 2
        j += 1

    k = 15

    while k <= 41:
        x = k - 5
        y = k - 10
        z = k - 15
        if grid[k] == 2 and grid[x] == 2 and grid[y] == 2 and grid[z] == 2:
            win = 2
        k += 1

    l = 0

    while l <= 38:
        x = l + 1
        y = l + 2
        z = l + 3
        if grid[l] == 2 and grid[x] == 2 and grid[y] == 2 and grid[z] == 2:
            win = 2
        l += 1
    # this is for player 2
    i = 21


    while  i <= 41:
        x = i - 7
        y = i - 14
        z = i - 21
        if grid[i] == 1 and grid[x] == 1 and grid[y] == 1 and grid[z] == 1:
            win = 5
        i += 1

    j = 18

    while j <= 41:
        x = j - 6
        y = j - 12
        z = j - 18
        if grid[j] == 1 and grid[x] == 1 and grid[y] == 1 and grid[z] == 1:
            win = 5
        j += 1

    k = 15

    while k <= 41:
        x = k - 5
        y = k - 10
        z = k - 15
        if grid[k] == 1 and grid[x] == 1 and grid[y] == 1 and grid[z] == 1:
            win = 5
        k += 1

    l = 0

    while l <= 38:
        x = l + 1
        y = l + 2
        z = l + 3
        if grid[l] == 1 and grid[x] == 1 and grid[y] == 1 and grid[z] == 1:
            win = 5
        l += 1
def AITurn():
    global turn
    c = random.randint(0,5)
    if grid[c + 36] == 0:
        grid[c + 36] = 2
    elif grid[c + 30] == 0:
        grid[c + 30] = 2
    elif grid[c + 24] == 0:
        grid[c + 24] = 2
    elif grid[c + 18] == 0:
        grid[c + 18] = 2
    elif grid[c + 12] == 0:
        grid[c + 12] = 2
    elif grid[c + 6] == 0:
        grid[c + 6] = 2
    elif grid[c] == 0:
        grid[c] = 2
    turn = 3

# Main Menu =================================================================
while gameOver == False and MainMenu == True:
    gameOver = pscreen.update()
    mpos = pscreen.getMousePosition()
    if pscreen.isKeyDown("escape"):
       gameOver = True

    pygame.draw.rect(pscreen.screen, (0,255,0), (0,0,480,660))
    pygame.draw.rect(pscreen.screen, (255,0,0), (120,132,240,140))
    pygame.draw.rect(pscreen.screen, (255,0,0), (120,390,240,140))
    pscreen.drawText("Courier New", 20, "Player vs. player", 240, 460, \
                         (255,255,255), "middle", "middle", \
                         None)
    pscreen.drawText("Courier New", 24, "Player vs. AI", 240, 202, \
                         (255,255,255), "middle", "middle", \
                         None)
    if pscreen.isMouseButtonDown("left") == True:
        if click == False:
            if click == False and  mpos[1] > 132 and mpos[1] < 272 and mpos[0] > 120 and mpos[0] < 360:
                pvp = False
                MainMenu = False
            if pscreen.isMouseButtonDown("left") == True and mpos[1] > 390 and mpos[1] < 530 and mpos[0] > 120 and mpos[0] < 360:
                pvp = True
                MainMenu = False
            click = True
    else:
        click = False

    pygame.display.flip()
# Game Loop =================================================================
while gameOver == False:
    timer += pscreen.deltaTime
    gameOver = pscreen.update()
    mpos = pscreen.getMousePosition()
    checkForWin()
    if pscreen.isKeyDown("escape"):
       gameOver = True
    if turn == 2 and timer >= 7 and win == False and pvp == False:
        AITurn()
        timer = random.randint(1,4)

    # Non-user Updates =========================================================
    for i, g in enumerate(grid):
        if g == 3:
            j = i * 80
            x = j % 480
            y = (int(j / 480) * 80) + 4
            color = 3
            animation = False
            list = (x,y,color,animation)
            coins.append(list)
        if g == 2:
            j = i * 80
            x = j % 480
            y = (int(j / 480) * 80) + 4
            color = 2
            animation = False
            list = (x,y,color,animation)
            coins.append(list)
        if g == 1:
            j = i * 80
            x = j % 480
            y = (int(j / 480) * 80) + 4
            color = 2
            animation = False
            list = (x,y,color,animation)
            coins.append(list)



    # User-input updates ========================================================

          # Checks for clicks
    if pscreen.isMouseButtonDown("left") == True:
        if click == False:
            x = turn
            if click == False and mpos[0] > 0 and mpos[0] < 80 and turn != 2 and win == False:
                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                timer = random.randint(1,4)
                c = 0
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue

                elif grid[c] == 0:
                    grid[c] = x

            if click == False and mpos[0] > 80 and mpos[0] < 160 and turn != 2 and win == False:
                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                c = 1
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue

                elif grid[c] == 0:
                    grid[c] = x

                timer = random.randint(1,4)
            if click == False and mpos[0] > 160 and mpos[0] < 240 and turn != 2 and win == False:

                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                c = 2
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue
                elif grid[c] == 0:
                    grid[c] = x
                timer = random.randint(1,4)
            if click == False and mpos[0] > 240 and mpos[0] < 320 and turn != 2 and win == False:
                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                c = 3
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue
                elif grid[c] == 0:
                    grid[c] = x

                timer = random.randint(1,4)
            if click == False and mpos[0] > 320 and mpos[0] < 400 and turn != 2 and win == False:
                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                c = 4
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue
                elif grid[c] == 0:
                    grid[c] = x

                timer = random.randint(1,4)
            if click == False and mpos[0] > 400 and mpos[0] < 4800 and turn != 2 and win == False:
                if pvp == True and turn == 3:
                    turn = 1
                elif pvp == True and turn == 1:
                    turn = 3
                else:
                    turn = 2
                c = 5
                if turn == 1:
                    x = 1
                if turn == 3:
                    x = 3
                if grid[c + 36] == 0:
                    grid[c + 36] = x
                elif grid[c + 30] == 0:
                    grid[c + 30] = x
                elif grid[c + 24] == 0:
                    grid[c + 24] = x
                elif grid[c + 18] == 0:
                    grid[c + 18] = x
                elif grid[c + 12] == 0:
                    grid[c + 12] = x
                elif grid[c + 6] == 0:
                    grid[c + 6] = x
                elif grid[c] != 0:
                    if pvp == True and turn == 3:
                        turn = 1
                    elif pvp == True and turn == 1:
                        turn = 3
                    else:
                        turn = 2
                    continue
                elif grid[c] == 0:
                    grid[c] = x

                timer = random.randint(1,4)


            click = True
    else:
        click = False


    # Drawing Code ==============================================================
    pscreen.screen.fill((0,0,100))

    for hole in holes:
        pygame.draw.circle(pscreen.screen, (125,125,125), (hole[0], hole[1]), 36)
        pygame.draw.circle(pscreen.screen, (255,255,255), (hole[0] - 4, hole[1]), 35)
    for coin in coins:
        x = coin[0]
        y = coin[1]
        if coin[2] == 3:
            section = (0,0,72,72)
        else:
            section = (72,0,72,72)
        pscreen.screen.blit(checkers, (x,y), section)


    coins = []

    # End Stuff =================================================================

    if win == True and pvp == False:
        s = pygame.Surface((480,560), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0,0,255,178))                         # notice the alpha value in the color
        pscreen.screen.blit(s, (0,0))
        pscreen.update()
        pscreen.drawText("Courier New", 24, "Congratz!, You Win!!!!", 240, 280, \
                         (255,255,255), "middle", "middle", \
                         None)
    if win == True and pvp == True:
        s = pygame.Surface((480,560), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0,0,255,178))                         # notice the alpha value in the color
        pscreen.screen.blit(s, (0,0))
        pscreen.update()
        pscreen.drawText("Courier New", 24, "Player 1 wins!", 240, 280, \
                         (255,255,255), "middle", "middle", \
                         None)
    if win == 2:
        s = pygame.Surface((480,560), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,0,0,178))                         # notice the alpha value in the color
        pscreen.screen.blit(s, (0,0))
        pscreen.update()
        pscreen.drawText("Courier New", 24, "you lost against this AI?!", 240, 280, \
                         (255,255,255), "middle", "middle", \
                         None)
    if win == 5:
        s = pygame.Surface((480,560), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((0,255,0,178))                         # notice the alpha value in the color
        pscreen.screen.blit(s, (0,0))
        pscreen.update()
        pscreen.drawText("Courier New", 24, "Player 2 wins!", 240, 280, \
                         (255,255,255), "middle", "middle", \
                         None)
    if turn == 3:
       pscreen.drawText("Courier New", 24, "Player", 240, 600, \
                         (255,255,255), "middle", "middle", \
                         None)
    if turn == 2 and win == False:
        pscreen.drawText("Courier New", 24, "AI: \"hummm... let me see.\"", 240, 600, \
                         (255,255,255), "middle", "middle", \
                         None)
    if turn == 2 and win == True:
        pscreen.drawText("Courier New", 24, "AI: \"That was a great game!\"", 240, 600, \
                         (255,255,255), "middle", "middle", \
                         None)
    if turn == 1:
        pscreen.drawText("Courier New", 24, "Player 2", 240, 600, \
                         (255,255,255), "middle", "middle", \
                         None)
    pygame.display.flip()
pscreen.quit()