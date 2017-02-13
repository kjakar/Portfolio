string_number = "4.3"
real_number = 4.3

print (string_number * 3)
print (real_number * 3)
print (string_number + "abc")    #concatenation is adding two strings
# print (real_number + "abc")

print ("""abcdef
ghijkl""")

#you can't do the above with a single-qouted string
# print ("abcdef
#      ghijkl")


#note the use of "\n" escape sequence -- this adds a new line (like hitting the enter key) right after the 'f', but before the 'g'
print ("abcdef\nghijkl")

#escape characters to remember
#\n   : new line
#\t   : tab
#\\   : print a single backslash
#'\'' : print a single qoute
#'\"' : print a doubble qoute
print("/\t\\\n\\\t/")


#this program illustrates some new variables and assignment statments
x = 15
y = x + 10

print ("y ='s", y)
x = 30
print ("y ='s", y)
# note : this type of any variable can change. it is always based on the last assignment made to it
y = "abc"
print ("y ='s", y)

# augmented assingment opperators
# +=, -=, /=, **=
# x = x + 1   will add one to the curent value of x
# x += 1      will do the same as above
print (x) #30
x = x + 1
print (x) #31
x += 1
print (x) #32
x -= 10
print (x) #22
x **= 2
print (x) #484

# new operators; %, //
# % is named modulo (remander)
print ("x % 2 =", x % 2)
print ("x % 2 =", x % 3)

# // is an interger devide (drops any decimal and does not round up.)
print ("x / 3 =", x / 3)
print ("x / 3 =", x // 3)
print ("9 // 10 =", 9 // 10)


#BUILT-IN FUNCTIONS----------------------------------------------------------
#our own functions.

#inportant built-in functions
#min, max, round, print, input, str, int, float.

x = 10
y = x + 2
pi = 3.1414159265
c = 2.99792458e8 # the e8 raises this to the 8th power

print ("pi to three decimals is", round (pi, 3))
print ("pi to three decimals is", round (pi, 0))
print ("c to the nearest 1000th is", round (c, -3))
print (min(y, x ** 0.5))
print (max(y, x ** 0.5))



#real use of input
#name = input("enter your name here ") #name will hold the string the user enters
#age = input("enter your age here ")
#print ("hello \"", name, "\".", sep="", end="")
#print (" in one year you will be", int(age) + 1) #age is still a string after this

#DEFINEING YOUR OWN FUNCTIONS
def adder(a, b):    #a and b are perameters 9placeholders) that will be supplied when the function is called and passed ARGUMENTS

    c = a + b
    return c
x = adder(3, 4) # calling the adder function. 3 and 4 are the arguments (a and b)
y = adder("abcd", "efgh")
print ("x ='s", x)
print ("y ='s", y)















