import csv
from pygame import *

testData = [["Dave", 65],["bill",99],["chris",43],["Austin", 66]]
gameData = []
leaderboard = []

class LeaderBoard(object):

    def __init__(self):
        #self.testData = [["Dave", 65],["bill",99],["chris",43],["Austin", 66]]
        self.gameData = []
        self. leaderBoard = []

    def writeScore(self, w_list):
        with open ("leaderboard.txt", "w") as db:
            dbw = csv.writer(db, lineterminator = "\n")
            for row in w_list:
                dbw.writerow(row)

    def readScore (self, r_list):
        with open ("leaderboard.txt", "r") as db:
            dbr = csv.reader(db)
            for row in dbr:
                tempList = []
                for item in row:
                    tempList.append(item)
                r_list.append(tempList)

    def leaderboardSort(self, leaderboard):
        lessThanPivot = []
        equalToPivot = []
        greaterThanPivot = []
        if len(leaderboard) > 1:
            pivot = int(leaderboard[0][1])
            for user in leaderboard:
                score = user[1]
                if score > pivot:
                    lessThanPivot.append(user)
                if score == pivot:
                    equalToPivot.append(user)
                if score < pivot:
                    greaterThanPivot.append(user)
            return self.leaderboardSort(lessThanPivot) + equalToPivot + self.leaderboardSort(greaterThanPivot)
        else:
            return leaderboard
    
    def render(self,surface, font):
        global leaderboard
        x = 210
        for i in range(len(leaderboard)):
            text = font.render(str(leaderboard[i]), True, (255,255,255))
            surface.blit(text,(x,15))
            x += 150
        

x = LeaderBoard()
testData = x.leaderboardSort(testData)
x.writeScore(testData)
x.readScore(leaderboard)

print(leaderboard)

