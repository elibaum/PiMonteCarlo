import random
import math

pointnum = 0.0
def isinside(x,y):
    global pointnum
    if math.sqrt(x**2+y**2) < 1:
        pointnum = pointnum + 1
q = input("How many point would you like to place?: ")
for x in range(0,q):
    isinside(random.random(),random.random())
print ((pointnum/q)* 4)
print str(100*(abs((((pointnum/q)* 4)-math.pi)/math.pi)))+ ' % off'