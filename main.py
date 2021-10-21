import math
from random import randint
def mcpi(N):
    #thewrhtika exw tous aksones x kai y me arithmous 0<x or y<100.
    counter = 0
    for i in range(N): #pairnw tuxaio shmeio me 2 suntetagmenes xi yi
        xi = randint(0, 100)
        yi = randint(0, 100)
        result = check(xi, yi)
        if result == True:
            counter = counter + 1
    logos = float(counter/N)
    p = float(logos*4)
    return p
#def mcpi2(N):
    #thewrhtika exw tous aksones x kai y me arithmous 0<(x or y)<100.
    #counter = 0
    #for i in range(N): #pairnw tuxaio shmeio me 2 suntetagmenes xi yi
        #xi = randint(0, 100)
        #yi = randint(0, 100)
        #result = check(xi, yi)
        #if result == True:
            #counter = counter + 1
    #logos = float((math.pi*2500)/(2500*4))
    #p = float(logos*4)
    #return p
def check(x, y): #sunarthsh pou elegxei an to shmeio einai entos h ektos kuklou.
    distance = 0
    if x < 50 and y < 50:
        x = 50 - x
        y = 50 - y
    elif x < 50 and y > 50:
        x = 50 - x
        y = y - 50
    elif x > 50 and y > 50:
        x = x - 50
        y = y - 50
    elif x > 50 and y < 50:
        x = x - 50
        y = 50 - y
    distance = x**2 + y**2 # puthagwreio thewrhma logw orthogwniou trigwnou
    if float(math.sqrt(distance)) <= 50:
        return True
    return False

print('for N = 10 : pi = ', mcpi(10), ' , real pi = ', math.pi)
print('for N = 100 : pi = ', mcpi(100), ' , real pi = ', math.pi)
print('for N = 1000 : pi = ', mcpi(1000), ' , real pi = ', math.pi)
print('for N = 3300 : pi = ', mcpi(3300), ' , real pi = ', math.pi)
print('for N = 10000 : pi = ', mcpi(10000), ' , real pi = ', math.pi)
