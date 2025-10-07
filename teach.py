# python teaching file
x = [1,2,3,4,5]  # a collection of nums
y = [2,3,4,5,29] # a collection of numbers

def sum(x):     # fxn name: sum, one input of x
    r = 0       # r is defined as zero
    for i in x: # i will at some point represent all values of x
        r = r+i # r is our continuing sum
    return r    # stating that sum returns r

print(sum(y))
print(sum(x))

def rational(x,y):                      # fxn with two inputs x & y
    if int(x) < 0.0 or int(y) <= 0.0:   # condition x < 0 and y <= 0
        return 0                        # should either fail return 0
    else:
        return (int(x)/int(y))          # should both pass return the rational x/y


def build_integers(x):
    if x > 0:
        for i in range(0,x):
            print(i*-1)
    else:
        print("x is not greater than zero")

print(build_integers(25))
