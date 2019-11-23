def make_bricks(small, big, goal):
    big_inch =  big * 5
    check = (goal - small)
    check = check / 5
    print(check)
    if check != int(check):
       print(False)
    elif small + big_inch < goal:
        print(False)
    elif goal // 5 <= big and goal % 5 <= small:
        print(True) 
    elif (goal - small) // 5 <= big:
        print(True)
    elif small + big_inch < goal:
        return False
    else:
        return False
make_bricks(2, 1000000, 100003)