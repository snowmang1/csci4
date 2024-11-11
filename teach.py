# control flow
import random

x = random.randint(0,10)
y = x/2
c = x**2

def maybe(x,y,z):
    if z:
        return "x is zero"
    else:
        return "x is not zero"

print(maybe(x, y, c==x and y==x))
# print(maybe(x, y, x==0))
