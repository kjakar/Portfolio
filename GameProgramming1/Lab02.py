# Alex Jones
# lab02

def makeArt():

    print ("   __  __")
    print ("  /  \\/  \\")
    print (" |        |")
    print ("  \      /")
    print ("   \    /")
    print ("    \  /")
    print ("     \/")
    print ("~~~~~~~~~~~~~")

def calculateForce(m1, m2, d):

    G = 6.67384e11
    forceMagnitude = G * ( (int(m1) * int(m2))/(int(d) ** 2))

    return forceMagnitude
    

def drawHPBar(hp_cur, hp_max):
    print ("|----------------------------------------|")
    print ("|", "<3" * (round(int(hp_cur) * 100 / int(hp_max)) // 5), "--" * (round((int(hp_max) - int(hp_cur)) * 100 / int(hp_max)) // 5), "|", sep="")
    print ("|----------------------------------------|")
    #I can't figure out how to make the "|" always be at the very end. the way I have it now works in most cases but not all
    #(for example, 100 max and 22 current) is there any way to fix that?

mass1 = input("What is the mass of object 1?")
mass2 = input("What is the mass of object 2?")
distance = input("What is the distance between the two objects")
maxHP = input("What is you characters max HP?")
curHP = input("What is you characters current HP?")



print(calculateForce(mass1, mass2, distance), drawHPBar(curHP, maxHP), makeArt())
input("Press Enter to continue")


