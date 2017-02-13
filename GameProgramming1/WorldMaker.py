__author__ = 'Alex Jones'


mapData = [["empty"]]
forLen = open(".\\saves\\mapInfo.txt", "r")
mapFileLen = sum(1 for line in forLen)

mapFile = open(".\\saves\\mapInfo.txt", "r")

layerDic = {}
newName = ""
newList = []
intList = []
needOut = False
oldTemp = "empty"
mapWidth = 30
mapHeight = 15
spriteW = 32
spriteH = 32

#This is the code that pulls all the data from the map text
for line in mapFile:

    if "[header]" in line: #this handles the information in the header
        print("inside header")

    if "[tilesets]" in line: # this handle the information about the tilesets
        print("inside tilesets")

    if "[layer]" in line or "[layer]" in oldTemp: #this appends the layers to the dictionary

        if needOut == False: # this is how I save the name of each layer with multiple loops
            newName = mapFile.readline()[5:-1]

        for i in range(mapFileLen):

            temp = mapFile.readline() #this holds the line that the code below works with, I do this to keep the line from moving lines when I don't want it to

            if needOut == True:
                needOut = False

            if "data=" in temp: #this avoids this usless line in that code ( as if we didn't know that 450 numbers were "data=" lol)
                pass

            if "[layer]" in temp: #this breaks the loop and add the list of the data to the dictionary
                oldTemp = "[layer]"
                needOut = True

                for i in range(15):
                    newList[i][0] = newList[i][0].split(",")
                    for x in range(mapWidth):
                        newList[i][0][x] = int(newList[i][0][x])




                layerDic[newName] = newList

                newName = mapFile.readline()[5:-1]

                newList = []

                break
            if len(temp) < 1: # this section deals with empty lines, although you can't use spaces 1-9 or my code won't work ( I need to add exceptios for each of these numbers)
                if '0' in temp or '1' in temp or '2' in temp or '3' in temp or '4' in temp or '5' in temp or '6' in temp or '7' in temp or '8' in temp or '9' in temp:
                    continue
                else:
                    break

            elif "data=" not in temp and "_" not in temp: # this adds the data from each line to a list and removes the "\n" from the end of the line
                newList.append(temp.splitlines())

            oldTemp = temp #this is for a trick to help with multiple layers


layerDic[newName] = newList
mapFile.close()

# end of colecting data ^================================================================= start of manipulating data ;)


import math
import pygame
import random


pygame.image.load(".\\saves\\mapSprite.png")
print(layerDic)

class mapController(object):

    def __init__(self, widthAndHeight):
        """
        this expects no more than 5 layers in you Mapinfo.txt, with the names, background, background2, foreground, clouds, and main.
        :param widthAndHeight: the width and height of the screen you are bliting the map to
        :return: This returns nothing (unless you count happieness ;) )
        """
        self.maxWidth = widthAndHeight[0]
        self.maxHeight = widthAndHeight[1]


    def render(self,pos, deltaTime, surface):
        for




































