import math
# this is a python file.
squid = 0 # name: squid, value: 0, type: Number
asdf = 100 # name: asdf, value: 100, type: Number

# types: Numbers, Letters, Booleans, Collections

# binding: name (collection of symbols),
#          value,
#          type,

binding1 = "hello" # name: binding1, value: hello, type: Collection<letter>
binding2 = "world"
#print(binding1, binding2)

# keyword def, name, parameters :
def f(a,b):
    c = a + b
    return c
# name: f, type: Number, Parameters: (a, b)
# Logic: line 17

print("c equals", f(5,5))

def fs(a,b):
    return a - b

print("fs is", fs(10,5))

def pyth(a,b):
    s1 = a**2
    s2 = b**2
    c  = math.sqrt(s1 + s2)
    return c

def pyth1(a,b):
    return math.sqrt(a**2 + b**2)

print("pyth of 4 4", pyth(4,4))
print("pyth1 of 4 4", pyth1(4,4))
