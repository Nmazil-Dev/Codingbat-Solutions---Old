def lone_sum(a, b, c):
    sum = a + b + c
    if a == b and a == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    if a == b and a == c:
        return 0
    else:
        return sum