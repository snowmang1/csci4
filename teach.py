#python file, itteration
#for looping

S = [1,2,3]
# 1 + 2 + 3 = 6

def summate(col):
    s = 0
    for x in col:
        s = s + x
    return s

def count_to_ten():
    s = []
    for x in range(0,9):
        s.append(x)
    return s

print(count_to_ten())
