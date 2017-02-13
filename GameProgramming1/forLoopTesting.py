for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)

print ("Good bye!")


edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

n = 5

sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print("Sum of 1 until %d: %d" % (n,sum))


for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
