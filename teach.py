# lucas numbers
def lucas(named_variable):
    omar = [2, 1]
    # 0 -> 2, 1 -> 1
    for n in range(2, named_variable):
        # for n which is equal to 2, 3, 4, 5
        omar.append(omar[n - 1] + omar[n - 2])
    return omar


print(lucas(1000000000))
