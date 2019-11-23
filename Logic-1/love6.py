def love6(a,b):
    sum = a + b
    diff = abs(a - b)
    if a == 6 or b == 6:
        return True
    elif sum == 6 or diff == 6:
        return True
    else:
        return False