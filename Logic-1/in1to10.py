def in1to10(n, outside_mode):
    if n in range(1, 11) and not outside_mode:
        return True
    elif n not in range(1,10) and not outside_mode:
        return False
    elif outside_mode and n <= 1 or n >= 10:
        return True
    else:
        return False