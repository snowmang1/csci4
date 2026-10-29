# file explaining function creation and use.

s1 = {0,1,2}
s2 = {0,2,4}

# function should multiply by two
# f(x) = 2x

def f(x):
    return 2*x

print("genious function f", f(2))

def f2(squid: int, banana: int) -> int:
    return squid+banana

print(f2("a", "b"))
