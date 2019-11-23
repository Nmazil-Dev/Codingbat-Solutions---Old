def near_ten(num):
    div = num % 10
    if div >= 8 or div <= 2:
        return True
    else:
        return False