def close_far(a, b, c):
    if a - 1 == b or c or a + 1 == b or c and a + 2 <= b or c or a -2 >= b or c:
        return True
    elif b - 1 == a or c or b -1 == a or c and b +2 <= a or c or  b -2 >= a or c:
        return True
    elif c - 1 == a or b or c +1 == a or b and c +2 <= a or b or c -2 >= a or b:
        return True
    else:
        return False