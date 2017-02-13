# Alex Jones
# Lab01



fname = "Alex"
lname = "Jones"
number = 21.6
hours = 9
minutes = 47
seconds = ((hours * 60 + 47) * 60)
radius = 8
cost = 12.99



print (fname, lname)
print (fname, lname, sep= ":")
print ("The cube-root of", number, "is", (number ** (1/3)),)
print ("There are", seconds, "seconds in", hours, "hours and", minutes, "minutes")
print ("The cost per square inch of a", (radius* 2), "inch diameter $", cost, "pizza is (in cents)", (3.14 *(radius ** 2) / cost))
input ("Press Enter to quit...")



#For some reason, when I hit enter to quit it some times it will paste what ever is in the clipboard.
